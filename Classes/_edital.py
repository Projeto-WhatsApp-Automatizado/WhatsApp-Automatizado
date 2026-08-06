from datetime import date
from pydantic import BaseModel, Field

class Edital(BaseModel):
    nome: str = Field(min_length=3)
    descricao: str = Field(min_length=1)
    data_prova: date
    banca: str = Field(min_length=3)
    data_cadastro: date
    ativo: bool