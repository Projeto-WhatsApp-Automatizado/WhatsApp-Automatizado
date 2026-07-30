from datetime import date
from pydantic import BaseModel, Field

class Curso(BaseModel):
    edital_id: str = Field(min_length=1)
    nome: str = Field(min_length=1)
    descricao: str = Field(min_length=1)
    carga_horaria: str = Field(min_length=1)
    valor: float = Field(gt=0)
    inicio_aulas: date
    status: bool