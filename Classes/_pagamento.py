from datetime import date

from pydantic import BaseModel, Field, field_validator


class Pagamento(BaseModel):
    valor: float = Field(gt=0)

    forma_pagamento: str = Field(
        min_length=2,
        max_length=30
    )

    data_pagamento: date

    observacoes: str = Field(
        min_length=3,
        max_length=255
    )

    matricula_id: int = Field(gt=0)

    ativo: bool

    @field_validator("forma_pagamento")
    @classmethod
    def validar_forma_pagamento(cls, valor: str):
        valor = valor.strip().upper()

        formas_validas = {
            "PIX",
            "BOLETO",
            "DINHEIRO",
            "CARTAO DE CREDITO",
            "CARTAO DE DEBITO"
        }

        if valor not in formas_validas:
            raise ValueError(
                "Forma de pagamento inválida. Utilize: PIX, BOLETO, DINHEIRO, CARTAO DE CREDITO ou CARTAO DE DEBITO."
            )

        return valor

    @field_validator("observacoes")
    @classmethod
    def validar_observacoes(cls, valor: str):
        valor = valor.strip()

        if not valor:
            raise ValueError("As observações não podem estar vazias.")

        return valor

    @field_validator("data_pagamento")
    @classmethod
    def validar_data(cls, valor: date):
        if valor > date.today():
            raise ValueError("A data de pagamento não pode ser futura.")

        return valor
