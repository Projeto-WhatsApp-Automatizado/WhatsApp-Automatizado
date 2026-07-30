from fastapi import APIRouter
from _atendimento import Atendimento


#pip install sqlalchemy
from sqlalchemy import create_engine, text
router = APIRouter(prefix="/atendimentos", tags=["at"])

#inserção no banco "postgresql://usuario:senha@servidor:porta/banco"
DATABASE_URL = "postgresql://postgres:123@localhost:5432/Zap?client_encoding=win1252"
#REST
#Create
@router.post('/cadastro')
def cadastrar(adm: Adm):

    engine = create_engine(DATABASE_URL)

    try:
        with engine.begin() as con:

            sql = """
                INSERT INTO public.administrador(
	                nome, email, senha, nivel_acesso, data_cadastro, status)
	            VALUES (:adm_nome, :adm_email, :adm_senha, :adm_acesso, :adm_cadastro, :adm_status);
            """

            dados = {
                "adm_nome": adm.nome,
                "adm_email": adm.email,
                "adm_senha": adm.senha,
                "adm_acesso": adm.nivel_acesso,
                "adm_cadastro": adm.data_cadastro,
                "adm_status": adm.status
            }

            con.execute(text(sql), dados)

            return {
                "mensagem": "Administrador cadastrado com sucesso"
            }

    except Exception as e:
        print(repr(e))
        return {
            "erro": str(e)
        }

    finally:
        engine.dispose()


@router.put('/{id}')
def atualizar(id: int, adm: Adm):

    engine = create_engine(DATABASE_URL)

    try:
        with engine.begin() as con:

            sql = """
                UPDATE public.administrador
	            SET nome=:adm_nome, email=:adm_email, senha=:adm_senha, nivel_acesso=:adm_acesso, data_cadastro=:adm_cadastro, status=:adm_status
	            WHERE id = :adm_id;
            """

            dados = {
                "adm_id": id,
                "adm_nome": adm.nome,
                "adm_email": adm.email,
                "adm_senha": adm.senha,
                "adm_acesso": adm.nivel_acesso,
                "adm_cadastro": adm.data_cadastro,
                "adm_status": adm.status
            }

            resultado = con.execute(text(sql), dados)

            if resultado.rowcount == 0:
                return {
                    "Administrador não encontrado"
                }

            return {
                "Administrador atualizado com sucesso"
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
                DELETE FROM public.administrador
	            WHERE id = :adm_id;
            """

            dados = {
                "adm_id": id
            }

            resultado = con.execute(text(sql), dados)

            if resultado.rowcount == 0:
                return {
                    "Administrador não encontrado"
                }

            return {
                "Administrador excluído com sucesso"
            }

    except Exception as e:
        return {
            "erro": str(e)
        }

    finally:
        engine.dispose()