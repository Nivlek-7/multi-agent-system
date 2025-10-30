from fastapi import FastAPI
from src.api import routes

# instância principal da aplicação
app = FastAPI(
    title="Gerador de Artigos com CrewAI",
    description="API para o sistema multiagente CrewAI para geração de artigos.",
    version="0.1.0",
)

# inclui as rotas do modulo api
app.include_router(routes.router)

