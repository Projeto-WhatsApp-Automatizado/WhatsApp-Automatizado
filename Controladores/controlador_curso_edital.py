from fastapi import APIRouter
from Classes._curso_edital import CursoEdital


#pip install sqlalchemy
from sqlalchemy import create_engine, text
router = APIRouter(prefix="/cursos-editais", tags=["cursos editais"])

#inserção no banco "postgresql://usuario:senha@servidor:porta/banco"
DATABASE_URL = "postgresql://postgres:123@localhost:5432/Zap?client_encoding=win1252"
#REST
#Create
@router.post('/cadastro')
def cadastrar(curso_edital: CursoEdital):

    engine = create_engine(DATABASE_URL)

    try:
        with engine.begin() as con:

            sql = """
                INSERT INTO public.curso_edital(
	                curso_id, edital_id)
	            VALUES (:curso_id, :edital_id);
            """

            dados = {
                "curso_id": curso_edital.curso_id,
                "edital_id": curso_edital.edital_id
            }

            con.execute(text(sql), dados)

            return {
                "mensagem": "CursoEdital cadastrado com sucesso"
            }

    except Exception as e:
        print(repr(e)) # Printa o erro cru no terminal do VS Code
        return {
            "erro": str(e)
        }

    finally:
        engine.dispose()


# @router.put('/')
# def atualizar( curso_edital: CursoEdital):

#     engine = create_engine(DATABASE_URL)

#     try:
#         with engine.begin() as con:

#             sql = """
#                 UPDATE public.curso_edital
# 	            SET curso_id=:curso_id, edital_id=:edital_id
# 	            WHERE curso_id = :curso_id AND edital_id = :edital_id;
#             """

#             dados = {
#                 "curso_id": curso_edital.curso_id,
#                 "edital_id": curso_edital.edital_id
#             }

#             resultado = con.execute(text(sql), dados)

#             if resultado.rowcount == 0:
#                 return {
#                     "CursoEdital não encontrado"
#                 }

#             return {
#                 "CursoEdital atualizado com sucesso"
#             }

#     except Exception as e:
#         return {
#             "erro": str(e)
#         }

#     finally:
#         engine.dispose()

@router.delete('/{curso_id}/{edital_id}')
def deletar(curso_id: int, edital_id: int):

    engine = create_engine(DATABASE_URL)

    try:
        with engine.begin() as con:

            sql = """
                DELETE FROM public.curso_edital
                WHERE curso_id = :curso_id
                  AND edital_id = :edital_id;
            """

            dados = {
                "curso_id": curso_id,
                "edital_id": edital_id
            }

            resultado = con.execute(text(sql), dados)

            if resultado.rowcount == 0:
                return {"mensagem": "Associação não encontrada"}

            return {"mensagem": "Associação removida com sucesso"}

    except Exception as e:
        return {"erro": str(e)}

    finally:
        engine.dispose()