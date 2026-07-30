import uvicorn
from fastapi import FastAPI

from controlador_usuario import router as usuarios_router
from controlador_editais import router as editais_router
from controlador_cursos import router as cursos_router

from controlador_adm import router as adm_router

app = FastAPI()

app.include_router(usuarios_router)
app.include_router(editais_router)
app.include_router(cursos_router)
app.include_router(adm_router)

if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        port = 80,
        reload=True
    )