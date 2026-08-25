from fastapi import APIRouter
from Classes._historico_chatbot import HistoricoChatbot
from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os

load_dotenv()

router = APIRouter(prefix="/historicos", tags=["Historicos"])

DATABASE_URL = os.getenv("DATABASE_URL")


@router.post("/cadastro")
def cadastrar(hist: HistoricoChatbot):

    engine = create_engine(DATABASE_URL)

    try:
        with engine.begin() as con:

            sql = """
                INSERT INTO public.historico_chatbot(
                    mensagem, resposta, data_hora, usuario_id)
                VALUES(:hist_mensagem, :hist_resposta, :hist_data_hora, :hist_usuario_id)
            """

            dados = {
                "hist_mensagem": hist.mensagem,
                "hist_resposta": hist.resposta,
                "hist_data_hora": hist.data_hora,
                "hist_usuario_id": hist.usuario_id
            }

            con.execute(text(sql), dados)

            return {
            "mensagem":"Histórico cadastrado com sucesso"
            }

    except Exception as e:
        print(repr(e))
        return {"erro":str(e)}

    finally:
        engine.dispose()


@router.put("/{id}")
def atualizar(id:int, hist:HistoricoChatbot):

    engine=create_engine(DATABASE_URL)

    try:
        with engine.begin() as con:

            sql="""
                UPDATE public.historico_chatbot
                SET mensagem=:hist_mensagem, resposta=:hist_resposta, data_hora=:hist_data_hora, usuario_id=:hist_usuario_id
                WHERE id=:hist_id;
            """

            dados = {
                "hist_id": id,
                "hist_mensagem": hist.mensagem,
                "hist_resposta": hist.resposta,
                "hist_data_hora": hist.data_hora,
                "hist_usuario_id": hist.usuario_id
            }

            resultado=con.execute(text(sql), dados)

            if resultado.rowcount==0:
                return {
                    "mensagem":"Histórico não encontrado"
                    }

            return {
                "mensagem":"Histórico atualizado com sucesso"
                }

    except Exception as e:
        return {"erro":str(e)}

    finally:
        engine.dispose()


@router.delete("/{id}")
def deletar(id:int):

    engine=create_engine(DATABASE_URL)

    try:

        with engine.begin() as con:

            sql="""
                DELETE FROM public.historico_chatbot
                WHERE id=:hist_id;
            """

            dados = {
                "int_id": id
            }

            resultado=con.execute(text(sql), dados)

            if resultado.rowcount==0:
                return {
                    "mensagem":"Histórico não encontrado"
                    }

            return {
                "mensagem":"Histórico excluído com sucesso"
                }

    except Exception as e:
        return {"erro":str(e)}

    finally:
        engine.dispose()