from datetime import date
from pydantic import BaseModel, Field

class Interesse(BaseModel):
    origem: str = Field(min_length=3)
    data: date
    usuario_id: int
    curso_id: int
    edital_id: int