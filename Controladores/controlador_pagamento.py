from fastapi import APIRouter
from Classes._pagamento import Pagamento
from dotenv import load_dotenv
import os

load_dotenv()

#pip install sqlalchemy
from sqlalchemy import create_engine, text
router = APIRouter(prefix="/pagamentos", tags=["pagamentos"])

#inserção no banco "postgresql://usuario:senha@servidor:porta/banco"
DATABASE_URL = os.getenv("DATABASE_URL")
#REST
#Create
@router.post('/cadastro')
def cadastrar(pag: Pagamento):

    engine = create_engine(DATABASE_URL)

    try:
        with engine.begin() as con:

            sql = """
                INSERT INTO public.pagamento(
	                valor, forma_pagamento, data_pagamento, observacoes, matricula_id, ativo)
	            VALUES (:pag_valor, :pag_forma, :pag_data, :pag_obs, :pag_matricula_id, :pag_ativo);
            """

            dados = {
                "pag_valor": pag.valor,
                "pag_forma": pag.forma_pagamento,
                "pag_data": pag.data_pagamento,
                "pag_obs": pag.observacoes,
                "pag_matricula_id": pag.matricula_id,
                "pag_ativo": pag.ativo
            }

            con.execute(text(sql), dados)

            return {
                "mensagem": "Pagamento cadastrado com sucesso"
            }

    except Exception as e:
        print(repr(e))
        return {
            "erro": str(e)
        }

    finally:
        engine.dispose()


@router.put('/{id}')
def atualizar(id: int, pag: Pagamento):

    engine = create_engine(DATABASE_URL)

    try:
        with engine.begin() as con:

            sql = """
                UPDATE public.pagamento
	            SET valor=:pag_valor, forma_pagamento=:pag_forma, data_pagamento=:pag_data, observacoes=:pag_obs, matricula_id=:pag_matricula_id, ativo=:pag_ativo
	            WHERE id = :pag_id;
            """

            dados = {
                "pag_id": id,
                "pag_valor": pag.valor,
                "pag_forma": pag.forma_pagamento,
                "pag_data": pag.data_pagamento,
                "pag_obs": pag.observacoes,
                "pag_matricula_id": pag.matricula_id,
                "pag_ativo": pag.ativo
            }

            resultado = con.execute(text(sql), dados)

            if resultado.rowcount == 0:
                return {
                    "Pagamento não encontrado"
                }

            return {
                "Pagamento atualizado com sucesso"
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
                DELETE FROM public.pagamento
	            WHERE id = :pag_id;
            """

            dados = {
                "pag_id": id
            }

            resultado = con.execute(text(sql), dados)

            if resultado.rowcount == 0:
                return {
                    "Pagamento não encontrado"
                }

            return {
                "Pagamento excluído com sucesso"
            }

    except Exception as e:
        return {
            "erro": str(e)
        }

    finally:
        engine.dispose()