from fastapi import APIRouter
from _historico_chatbot import HistoricoChatbot

from sqlalchemy import create_engine, text

router = APIRouter(prefix="/historico_chatbot", tags=["Historico Chatbot"])

DATABASE_URL = "postgresql://postgres:123@localhost:5432/Zap?client_encoding=win1252"


# POST
@router.post("/cadastro")
def cadastrar(chat: HistoricoChatbot):

    engine = create_engine(DATABASE_URL)

    try:
        with engine.begin() as con:

            sql = """
                INSERT INTO public.historico_chatbot
                (mensagem, resposta, data_hora, usuario_id)
                VALUES
                (:mensagem, :resposta, :data_hora, :usuario_id)
            """

            dados = {
                "mensagem": chat.mensagem,
                "resposta": chat.resposta,
                "data_hora": chat.data_hora,
                "usuario_id": chat.usuario_id
            }

            con.execute(text(sql), dados)

            return {"mensagem":"Histórico cadastrado com sucesso"}

    except Exception as e:
        print(repr(e))
        return {"erro":str(e)}

    finally:
        engine.dispose()


# PUT
@router.put("/{id}")
def atualizar(id:int, chat:HistoricoChatbot):

    engine=create_engine(DATABASE_URL)

    try:
        with engine.begin() as con:

            sql="""
                UPDATE public.historico_chatbot
                SET mensagem=:mensagem,
                    resposta=:resposta,
                    data_hora=:data_hora,
                    usuario_id=:usuario_id
                WHERE id=:id;
            """

            resultado=con.execute(
                text(sql),
                {
                    "id":id,
                    "mensagem":chat.mensagem,
                    "resposta":chat.resposta,
                    "data_hora":chat.data_hora,
                    "usuario_id":chat.usuario_id
                }
            )

            if resultado.rowcount==0:
                return {"mensagem":"Histórico não encontrado"}

            return {"mensagem":"Histórico atualizado com sucesso"}

    except Exception as e:
        return {"erro":str(e)}

    finally:
        engine.dispose()


# DELETE
@router.delete("/{id}")
def deletar(id:int):

    engine=create_engine(DATABASE_URL)

    try:

        with engine.begin() as con:

            sql="""
                DELETE FROM public.historico_chatbot
                WHERE id=:id;
            """

            resultado=con.execute(text(sql),{"id":id})

            if resultado.rowcount==0:
                return {"mensagem":"Histórico não encontrado"}

            return {"mensagem":"Histórico excluído com sucesso"}

    except Exception as e:
        return {"erro":str(e)}

    finally:
        engine.dispose()