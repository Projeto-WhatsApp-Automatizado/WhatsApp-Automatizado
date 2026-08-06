from datetime import date
from pydantic import BaseModel, Field

class Pagamento(BaseModel):
    valor: float = Field(gt=0)
    forma_pagamento: str = Field(min_length=2)
    status: str = Field(min_length=2)
    data_pagamento: date
    observacoes: str = Field(min_length=3)
    matricula_id: int