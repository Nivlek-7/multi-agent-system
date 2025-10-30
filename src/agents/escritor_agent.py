from crewai import Agent, Task, LLM
import os

llm = LLM(
    model="google/gemini-2.5-flash",
    api_key=os.getenv("GOOGLE_API_KEY"),
)

escritor = Agent(
    role="Escritor de Conteúdo",
    goal="Escrever um artigo de opinião perspicaz e factualmente "
        "preciso sobre o tópico: {topic}",
    backstory="Você está trabalhando na escrita "
              "de um novo artigo de opinião sobre o tema: {topic}. "
              "Você baseia sua escrita no trabalho do "
              "Pesquisador de Conteúdo, que fornece um esboço "
              "e contexto relevante sobre o tema. "
              "Você segue os principais objetivos e "
              "a direção do esboço, "
              "conforme fornecido pelo Pesquisador de Conteúdo. "
              "Você também apresenta análises objetivas e imparciais "
              "e as fundamenta com informações "
              "fornecidas pelo Pesquisador de Conteúdo. "
              "Você reconhece em seu artigo de opinião "
              "quando suas afirmações são opiniões "
              "em vez de declarações objetivas.",
    llm=llm,
    allow_delegation=False,
    verbose=True
)

escrever = Task(
    description=(
        "1. Use a pesquisa do conteúdo para criar um "
        "artigo envolvente para o website sobre {topic}.\n"
        "2. Incorpore palavras-chave de SEO de forma natural.\n"
        "3. As seções/subtítulos devem ser nomeados "
        "de maneira atrativa.\n"
        "4. Garanta que o artigo esteja estruturado com "
        "uma introdução envolvente, um corpo informativo "
        "e uma conclusão resumida.\n"
        "5. Assegure-se que o artigo tenha no mínimo 300 palavras."
        "6. Revise o texto para corrigir erros gramaticais e "
        "assegurar o alinhamento com o tom de voz da marca.\n"
    ),
    expected_output= "Um artigo bem escrito " 
        "pronto para ser publicado, "
        "cada seção deve conter 2 ou 3 parágrafos.",
    agent=escritor,
)