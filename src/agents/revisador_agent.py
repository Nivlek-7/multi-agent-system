from crewai import Agent, Task, LLM
from src.models.artigo_model import Artigo
import os

llm = LLM(
    model="google/gemini-2.5-flash",
    api_key=os.getenv("GOOGLE_API_KEY"),
)

revisador = Agent(
    role="Revisador de Conteúdo",
    goal="Edite um artigo de opinião existente do website para "
        "alinhar-se ao estilo de escrita da organização.",
    backstory="Você é um revisor que recebe um artigo de opinião "
              "do Escritor de Conteúdo. "
              "Seu objetivo é revisar o artigo de opinião "
              "para garantir que ele siga as melhores práticas jornalísticas, "
              "apresente pontos de vista equilibrados "
              "ao expor opiniões ou afirmações "
              "e também evite tópicos ou opiniões altamente controversos "
              "sempre que possível.",
    llm=llm,
    verbose=True
)

revisar = Task(
    description=("Revise o artigo de opinião fornecido para "
                 "verificar erros gramaticais e "
                 "o alinhamento com o tom de voz da marca."),
    expected_output="Um artigo de blog bem escrito, "
                    "pronto para publicação, "
                    "em que cada seção deve conter 2 ou 3 parágrafos "
                    "com mínimo de 300 palavras.",
    output_pydantic=Artigo,
    agent=revisador
)

