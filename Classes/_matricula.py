from datetime import date

from pydantic import BaseModel, Field, field_validator


class Matricula(BaseModel):
    data_matricula: date

    observacoes: str = Field(
        min_length=1,
        max_length=255
    )

    usuario_id: int = Field(gt=0)

    curso_id: int = Field(gt=0)

    ativo: bool

    @field_validator("observacoes")
    @classmethod
    def validar_observacoes(cls, valor: str):
        valor = valor.strip()

        if not valor:
            raise ValueError("As observações não podem estar vazias.")

        return valor

    @field_validator("data_matricula")
    @classmethod
    def validar_data_matricula(cls, valor: date):
        if valor > date.today():
            raise ValueError(
                "A data da matrícula não pode ser futura."
            )

        return valor