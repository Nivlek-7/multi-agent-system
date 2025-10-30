from crewai import Crew, LLM
import os
from src.agents.pesquisador_agent import pesquisador, pesquisar
from src.agents.escritor_agent import escritor, escrever
from src.agents.revisador_agent import revisador, revisar
from src.models.artigo_model import Artigo

llm = LLM(
    model="google/gemini-2.5-flash",
    api_key=os.getenv("GOOGLE_API_KEY"),
)

crew = Crew(
    agents=[pesquisador, escritor, revisador],
    tasks=[pesquisar, escrever, revisar],
    llm=llm,
    verbose=True
    #memory=True // foi necessário comentar por causa que puxava o serviço da OpenAi
)

async def gerar_artigo(topic: str) -> Artigo:
    """
    Gera um artigo completo sobre o tópico fornecido, executando a crew de agentes.
    Retorna um objeto Pydantic do tipo Artigo.
    """
    input_data = {"topic": topic}

    # Executa o crew assincronamente
    resultado = await crew.kickoff_async(inputs=input_data)

    # Se a última task tem output_pydantic, o Crew retorna diretamente o modelo validado
    if hasattr(resultado, "pydantic") and resultado.pydantic:
        return resultado.pydantic

    # Tenta usar o conteúdo bruto em caso de erro
    if hasattr(resultado, "raw_output"):
        raw = resultado.raw_output.strip()
        return Artigo(title=f"Artigo sobre {topic}", content=raw)

    raise ValueError("Nenhum resultado válido retornado pelo Crew.")
