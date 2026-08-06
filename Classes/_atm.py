from datetime import date

from pydantic import BaseModel, Field, field_validator


class Atm(BaseModel):
    assunto: str = Field(
        min_length=3,
        max_length=100
    )

    data_abertura: date

    data_fechamento: date | None = None

    usuario_id: int = Field(
        gt=0
    )

    ativo: bool

    @field_validator("assunto")
    @classmethod
    def validar_assunto(cls, valor: str):
        valor = valor.strip()

        if not valor:
            raise ValueError("O assunto não pode estar vazio.")

        return valor

    @field_validator("data_abertura")
    @classmethod
    def validar_data_abertura(cls, valor: date):
        if valor > date.today():
            raise ValueError(
                "A data de abertura não pode ser futura."
            )

        return valor

    @field_validator("data_fechamento")
    @classmethod
    def validar_data_fechamento(cls, valor: date | None):
        if valor and valor > date.today():
            raise ValueError(
                "A data de fechamento não pode ser futura."
            )

        return valor