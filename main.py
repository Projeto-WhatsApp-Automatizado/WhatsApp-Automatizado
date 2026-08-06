import uvicorn
from fastapi import FastAPI

from Controladores.controlador_usuario import router as usuarios_router
from Controladores.controlador_editais import router as editais_router
from Controladores.controlador_cursos import router as cursos_router
from Controladores.controlador_adm import router as adm_router
from Controladores.controlador_historico_chatbot import router as historio_chatbot_router
from Controladores.controlador_atm import router as atendimento_router
from Controladores.controlador_pagamento import router as pagamento_router

app = FastAPI()

app.include_router(usuarios_router)
app.include_router(editais_router)
app.include_router(cursos_router)
app.include_router(adm_router)
app.include_router(historio_chatbot_router)
app.include_router(atendimento_router)
app.include_router(pagamento_router)

if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        port = 80,
        reload=True
    )