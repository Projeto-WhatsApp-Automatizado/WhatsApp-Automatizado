from datetime import datetime

from pydantic import BaseModel, Field, field_validator


class HistoricoChatbot(BaseModel):
    mensagem: str = Field(
        min_length=1,
        max_length=1000
    )

    resposta: str = Field(
        min_length=1,
        max_length=5000
    )

    data_hora: datetime

    usuario_id: int = Field(gt=0)

    @field_validator("mensagem", "resposta")
    @classmethod
    def validar_texto(cls, valor: str):
        valor = valor.strip()

        if not valor:
            raise ValueError("O campo não pode estar vazio.")

        return valor

    @field_validator("data_hora")
    @classmethod
    def validar_data_hora(cls, valor: datetime):
        if valor > datetime.now():
            raise ValueError("A data e hora não podem ser futuras.")

        return valor