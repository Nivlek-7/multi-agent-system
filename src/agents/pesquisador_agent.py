from crewai import Agent, Task, LLM
from src.tools.wikipedia_tool import WikipediaTool
import os

llm = LLM(
    model="google/gemini-2.5-flash",
    api_key=os.getenv("GOOGLE_API_KEY"),
)

wiki_tool = WikipediaTool()

pesquisador = Agent(
    role="Pesquisador de Conteúdo",
    goal="Pesquisar conteúdo envolvente e factualmente preciso sobre {topic}",
    backstory="Você está trabalhando na coleta de dados para um website"
              "sobre o tópico: {topic}."
              "Você coletará informações que ajudam" 
              "o público a aprender alguma coisa" 
              "e a fazer decisões informadas"
              "utilizando a ferramenta que está a sua disposição."
              "O seu trabalho é a base para que"  
              "o Escritor do Conteúdo escreva um artigo de opinião sobre esse tópico.",
    llm=llm,
    tools=[wiki_tool],
    allow_delegation=False,
	verbose=True
)

pesquisar = Task(
    description=(
        "1. Dê preferência às últimas tendências "    
            "e assuntos em destaque nesse {topic}.\n"
        "2. Identifique o público alvo, considerando " 
            "os interesses deles e seus possíveis desafios.\n" 
        "3. Elabore um esboço de conteúdo detalhado, incluindo: "  
            "uma introdução, pontos-chave e uma chamada para ação(ou call to action).\n"
        "4. Inclua palavras-chave de SEO e dados relevantes ou recursos." 
    ),
    expected_output="Um documento abrangente com a pesquisa do conteúdo"
        "com um esboço, análise de público,"  
        "palavras-chave de SEO e recursos.",
    agent=pesquisador,
)