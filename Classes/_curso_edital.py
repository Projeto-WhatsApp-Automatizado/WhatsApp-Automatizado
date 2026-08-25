from datetime import date
from pydantic import BaseModel, Field, EmailStr

class CursoEdital(BaseModel):
    curso_id: int = Field(gt=0)
    edital_id: int = Field(gt=0)
