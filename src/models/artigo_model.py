from pydantic import BaseModel

# Modelo de dados utilizado para representar um artigo usando o Pydantic
class Artigo(BaseModel):
    title: str
    content: str