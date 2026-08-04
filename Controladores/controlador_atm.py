from fastapi import APIRouter
from _atm import Atm


#pip install sqlalchemy
from sqlalchemy import create_engine, text
router = APIRouter(prefix="/atms", tags=["atms"])

#inserção no banco "postgresql://usuario:senha@servidor:porta/banco"
DATABASE_URL = "postgresql://postgres:123@localhost:5432/Zap?client_encoding=win1252"
#REST
#Create
@router.post('/cadastro')
def cadastrar(atm: Atm):

    engine = create_engine(DATABASE_URL)

    try:
        with engine.begin() as con:

            sql = """
                INSERT INTO public.atendimento(
	                assunto, status, data_abertura, data_fechamento, usuario_id)
	            VALUES (:atm_assunto, :atm_status, :atm_abertura, :atm_fechamento, :atm_usuario_id);
            """

            dados = {
                "atm_assunto": atm.assunto,
                "atm_status": atm.status,
                "atm_abertura": atm.data_abertura,
                "atm_fechamento": atm.data_fechamento,
                "atm_usuario_id": atm.usuario_id
            }

            con.execute(text(sql), dados)

            return {
                "mensagem": "Atendimento cadastrado com sucesso"
            }

    except Exception as e:
        print(repr(e))
        return {
            "erro": str(e)
        }

    finally:
        engine.dispose()


@router.put('/{id}')
def atualizar(id: int, atm: Atm):

    engine = create_engine(DATABASE_URL)

    try:
        with engine.begin() as con:

            sql = """
                UPDATE public.atendimento
	            SET assunto=:atm_assunto, status=:atm_status, data_abertura=:atm_abertura, data_fechamento=:atm_fechamento, usuario_id=:atm_usuario_id
	            WHERE id = :atm_id;
            """

            dados = {
                "atm_id": id,
                "atm_assunto": atm.assunto,
                "atm_status": atm.status,
                "atm_abertura": atm.data_abertura,
                "atm_fechamento": atm.data_fechamento,
                "atm_usuario_id": atm.usuario_id
            }

            resultado = con.execute(text(sql), dados)

            if resultado.rowcount == 0:
                return {
                    "Atendimento não encontrado"
                }

            return {
                "Atendimento atualizado com sucesso"
            }

    except Exception as e:
        return {
            "erro": str(e)
        }

    finally:
        engine.dispose()

@router.delete('/{id}')
def deletar(id: int):

    engine = create_engine(DATABASE_URL)

    try:
        with engine.begin() as con:

            sql = """
                DELETE FROM public.atendimento
	            WHERE id = :atm_id;
            """

            dados = {
                "atm_id": id
            }

            resultado = con.execute(text(sql), dados)

            if resultado.rowcount == 0:
                return {
                    "Atendimento não encontrado"
                }

            return {
                "Atendimento excluído com sucesso"
            }

    except Exception as e:
        return {
            "erro": str(e)
        }

    finally:
        engine.dispose()