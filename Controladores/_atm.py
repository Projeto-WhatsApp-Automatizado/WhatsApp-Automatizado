from datetime import date
from pydantic import BaseModel, Field

class Atm(BaseModel):
    assunto: str = Field(min_length=3)
    status: str = Field(min_length=2)
    data_abertura: date
    data_fechamento: date
    usuario_id: int
