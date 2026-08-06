from datetime import date
from pydantic import BaseModel, Field, EmailStr

class CursoEdital(BaseModel):
    curso_id: int
    edital_id: int
