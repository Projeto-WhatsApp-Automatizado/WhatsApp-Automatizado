from pydantic import BaseModel, EmailStr, Field

class Usuario(BaseModel):
    nome: str = Field(min_length=3)
    email: EmailStr
    telefone: str = Field(min_length=11)
    estado: str = Field(min_length=3)
    interesse: str = Field(min_length=3)