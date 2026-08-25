from datetime import date

from pydantic import BaseModel, EmailStr, Field, field_validator

#classe de Administrador, com validações
class Adm(BaseModel):
    nome: str = Field(
        min_length=3,
        max_length=100
    )

    email: EmailStr

    senha: str = Field(
        min_length=8,
        max_length=100
    )

    nivel_acesso: str = Field(
        min_length=1,
        max_length=30
    )

    data_cadastro: date

    ativo: bool

    @field_validator("nome", "nivel_acesso")
    @classmethod
    def validar_textos(cls, valor: str):
        valor = valor.strip()

        if not valor:
            raise ValueError("O campo não pode estar vazio.")

        return valor

    @field_validator("senha")
    @classmethod
    def validar_senha(cls, valor: str):
        if not any(char.isupper() for char in valor):
            raise ValueError(
                "A senha deve conter pelo menos uma letra maiúscula."
            )

        if not any(char.islower() for char in valor):
            raise ValueError(
                "A senha deve conter pelo menos uma letra minúscula."
            )

        if not any(char.isdigit() for char in valor):
            raise ValueError(
                "A senha deve conter pelo menos um número."
            )

        return valor

    @field_validator("data_cadastro")
    @classmethod
    def validar_data_cadastro(cls, valor: date):
        if valor > date.today():
            raise ValueError(
                "A data de cadastro não pode ser futura."
            )

        return valor
