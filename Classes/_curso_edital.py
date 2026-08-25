from pydantic import BaseModel, Field

class CursoEdital(BaseModel):
    curso_id: int = Field(gt=0)
    edital_id: int = Field(gt=0)
