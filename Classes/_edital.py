from datetime import date

from pydantic import BaseModel, Field, field_validator


class Edital(BaseModel):
    nome: str = Field(
        min_length=3,
        max_length=100
    )

    descricao: str = Field(
        min_length=1,
        max_length=500
    )

    data_prova: date

    banca: str = Field(
        min_length=3,
        max_length=100
    )

    data_cadastro: date

    ativo: bool

    @field_validator("nome", "descricao", "banca")
    @classmethod
    def validar_textos(cls, valor: str):
        valor = valor.strip()

        if not valor:
            raise ValueError("O campo não pode estar vazio.")

        return valor

    @field_validator("data_prova")
    @classmethod
    def validar_data_prova(cls, valor: date):
        if valor < date.today():
            raise ValueError(
                "A data da prova não pode ser anterior à data atual."
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
