from pydantic import BaseModel, EmailStr, Field

class Usuario(BaseModel):
    nome: str = Field(
        min_length=3,
        max_length=100
    )

    email: EmailStr

    telefone: str = Field(
        pattern=r"^\d{11}$",
        description="Telefone com DDD e 11 dígitos, somente números"
    )

    estado: str = Field(
        pattern=r"^[A-Z]{2}$",
        description="Sigla do estado (ex: SP, RJ, MG)"
    )

    interesse: str = Field(
        min_length=3,
        max_length=100
    )