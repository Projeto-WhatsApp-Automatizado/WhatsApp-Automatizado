from pydantic import BaseModel
from datetime import datetime

class HistoricoChatbot(BaseModel):
    mensagem: str
    resposta: str
    data_hora: datetime
    usuario_id: int