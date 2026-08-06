from datetime import date
from pydantic import BaseModel, Field

class Matricula(BaseModel):
    data_matricula: date
    observacoes: str = Field(min_length=1)
    usuario_id: int = Field(gt=0)
    curso_id: int = Field(gt=0)
    ativo: bool
