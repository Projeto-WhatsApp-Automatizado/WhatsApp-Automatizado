from datetime import date
from pydantic import BaseModel, Field, EmailStr

class Adm(BaseModel):
    nome: str = Field(min_length=3)
    email: EmailStr
    senha: str = Field(min_length=8)
    nivel_acesso: str = Field(min_length=1)
    data_cadastro: date
    status: bool