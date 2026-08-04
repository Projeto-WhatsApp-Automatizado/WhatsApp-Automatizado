from fastapi import APIRouter
from _pagamento import Pagamento


#pip install sqlalchemy
from sqlalchemy import create_engine, text
router = APIRouter(prefix="/pagamentos", tags=["pagamentos"])

#inserção no banco "postgresql://usuario:senha@servidor:porta/banco"
DATABASE_URL = "postgresql://postgres:123@localhost:5432/Zap?client_encoding=win1252"
#REST
#Create
@router.post('/cadastro')
def cadastrar(pagamento: Pagamento):

    engine = create_engine(DATABASE_URL)

    try:
        with engine.begin() as con:

            sql = """
                INSERT INTO public.pagamento(
	                valor, forma_pagamento, status, data_pagamento, observacoes, matricula_id)
	            VALUES (:pag_valor, :pag_forma, :pag_status, :pag_data, :pag_obs, :pag_matricula_id);
            """

            dados = {
                "pag_valor": pagamento.valor,
                "pag_forma": pagamento.forma_pagamento,
                "pag_status": pagamento.status,
                "pag_data": pagamento.data_pagamento,
                "pag_obs": pagamento.observacoes,
                "pag_matricula_id": pagamento.matricula_id
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
def atualizar(id: int, pagamento: Pagamento):

    engine = create_engine(DATABASE_URL)

    try:
        with engine.begin() as con:

            sql = """
                UPDATE public.pagamento
	            SET valor=:pag_valor, forma_pagamento=:pag_forma, status=:pag_status, data_pagamento=:pag_data, observacoes=:pag_obs, matricula_id=:pag_matricula_id
	            WHERE id = :pag_id;
            """

            dados = {
                "pag_id": id,
                "pag_valor": pagamento.valor,
                "pag_forma": pagamento.forma_pagamento,
                "pag_status": pagamento.status,
                "pag_data": pagamento.data_pagamento,
                "pag_obs": pagamento.observacoes,
                "pag_matricula_id": pagamento.matricula_id
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