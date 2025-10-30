from fastapi import APIRouter
from fastapi.params import Query
from src.services.crew_service import gerar_artigo

router = APIRouter()

@router.get("/", tags=["Raíz"])
async def root():
    """
    Rota principal da API — usada para teste inicial.
    """
    return {"message": "Gerador de Artigo CrewAI está online!"}

@router.get("/artigo", tags=["Artigo"])
async def get_artigo(topico: str = Query(..., description="Tema para o artigo a ser gerado")):
    """
    Rota que recebe um parâmetro de tópico via URL.
    Exemplo: http://127.0.0.1:8000/article?topico=africa
    """
    
    artigo = await gerar_artigo(topic=topico)
    return artigo