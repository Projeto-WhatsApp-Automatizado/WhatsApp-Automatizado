from datetime import date

from pydantic import BaseModel, Field, field_validator


class Curso(BaseModel):
    nome: str = Field(
        min_length=1,
        max_length=100
    )

    descricao: str = Field(
        min_length=1,
        max_length=500
    )

    carga_horaria: int = Field(
        gt=0
    )

    valor: float = Field(
        gt=0
    )

    inicio_aulas: date

    ativo: bool

    @field_validator("nome", "descricao")
    @classmethod
    def validar_textos(cls, valor: str):
        valor = valor.strip()

        if not valor:
            raise ValueError("O campo não pode estar vazio.")

        return valor

    @field_validator("inicio_aulas")
    @classmethod
    def validar_inicio_aulas(cls, valor: date):
        if valor < date.today():
            raise ValueError(
                "A data de início das aulas não pode ser anterior à data atual."
            )

        return valor