from fastapi import APIRouter
from Classes._interesse import Interesse


#pip install sqlalchemy
from sqlalchemy import create_engine, text
router = APIRouter(prefix="/interesses", tags=["interesses"])

#inserção no banco "postgresql://usuario:senha@servidor:porta/banco"
DATABASE_URL = "postgresql://postgres:123@localhost:5432/Zap?client_encoding=win1252"
#REST
#Create
@router.post('/cadastro')
def cadastrar(int: Interesse):

    engine = create_engine(DATABASE_URL)

    try:
        with engine.begin() as con:

            sql = """
                INSERT INTO public.interesse(
	                origem, data, usuario_id, curso_id, edital_id)
	            VALUES (:int_origem, :int_data, :int_usuario_id, :int_curso_id, :int_edital_id);
            """

            dados = {
                "int_origem": int.origem,
                "int_data": int.data,
                "int_usuario_id": int.usuario_id,
                "int_curso_id": int.curso_id,
                "int_edital_id": int.edital_id
            }

            con.execute(text(sql), dados)

            return {
                "mensagem": "Interesse cadastrado com sucesso"
            }

    except Exception as e:
        print(repr(e))
        return {
            "erro": str(e)
        }

    finally:
        engine.dispose()


@router.put('/{id}')
def atualizar(id: int, int: Interesse):

    engine = create_engine(DATABASE_URL)

    try:
        with engine.begin() as con:

            sql = """
                UPDATE public.interesse
	            SET origem=:int_origem, data=:int_data, usuario_id=:int_usuario_id, curso_id=:int_curso_id, edital_id=:int_edital_id
	            WHERE id = :int_id;
            """

            dados = {
                "int_id": id,
                "int_origem": int.origem,
                "int_data": int.data,
                "int_usuario_id": int.usuario_id,
                "int_curso_id": int.curso_id,
                "int_edital_id": int.edital_id
            }

            resultado = con.execute(text(sql), dados)

            if resultado.rowcount == 0:
                return {
                    "Interesse não encontrado"
                }

            return {
                "Interesse atualizado com sucesso"
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
                DELETE FROM public.interesse
	            WHERE id = :int_id;
            """

            dados = {
                "int_id": id
            }

            resultado = con.execute(text(sql), dados)

            if resultado.rowcount == 0:
                return {
                    "Interesse não encontrado"
                }

            return {
                "Interesse excluído com sucesso"
            }

    except Exception as e:
        return {
            "erro": str(e)
        }

    finally:
        engine.dispose()