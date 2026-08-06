from datetime import date

from pydantic import BaseModel, Field, field_validator


class Interesse(BaseModel):
    origem: str = Field(
        min_length=3,
        max_length=100
    )

    data: date

    usuario_id: int = Field(gt=0)
    curso_id: int = Field(gt=0)
    edital_id: int = Field(gt=0)

    @field_validator("origem")
    @classmethod
    def validar_origem(cls, valor: str):
        valor = valor.strip()

        if not valor:
            raise ValueError("A origem não pode estar vazia.")

        return valor

    @field_validator("data")
    @classmethod
    def validar_data(cls, valor: date):
        if valor > date.today():
            raise ValueError("A data não pode ser futura.")

        return valor