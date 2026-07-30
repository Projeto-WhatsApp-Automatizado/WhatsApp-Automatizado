from fastapi import APIRouter
from _matricula import Matricula


#pip install sqlalchemy
from sqlalchemy import create_engine, text
router = APIRouter(prefix="/matricula", tags=["matriculas"])

#inserção no banco "postgresql://usuario:senha@servidor:porta/banco"
DATABASE_URL = "postgresql://postgres:123@localhost:5432/Zap?client_encoding=win1252"
#REST
#Create
@router.post('/cadastro')
def cadastrar(matricula: Matricula):

    engine = create_engine(DATABASE_URL)

    try:
        with engine.begin() as con:

            sql = """
                INSERT INTO public.matricula(
	                status, data_matricula, observacoes, usuario_id, curso_id)
	            VALUES (:status, :data_matricula, :observacoes, :usuario_id, :curso_id);
            """

            dados = {
                "status": matricula.status,
                "data_matricula": matricula.data_matricula,
                "observacoes": matricula.observacoes,
                "usuario_id": matricula.usuario_id,
                "curso_id": matricula.curso_id
            }

            con.execute(text(sql), dados)

            return {
                "mensagem": "Matrícula cadastrada com sucesso"
            }

    except Exception as e:
        print(repr(e)) # Printa o erro cru no terminal do VS Code
        return {
            "erro": str(e)
        }

    finally:
        engine.dispose()


@router.put('/{id}')
def atualizar(id: int, matricula: Matricula):

    engine = create_engine(DATABASE_URL)

    try:
        with engine.begin() as con:

            sql = """
                UPDATE public.matricula
	            SET status=:status, data_matricula=:data_matricula, observacoes=:observacoes, usuario_id=:usuario_id, curso_id=:curso_id
	            WHERE id = :matricula_id;
            """

            dados = {
                "matricula_id": id,
                "status": matricula.status,
                "data_matricula": matricula.data_matricula,
                "observacoes": matricula.observacoes,
                "usuario_id": matricula.usuario_id,
                "curso_id": matricula.curso_id
            }

            resultado = con.execute(text(sql), dados)

            if resultado.rowcount == 0:
                return {
                    "Matrícula não encontrada"
                }

            return {
                "Matrícula atualizada com sucesso"
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
                DELETE FROM public.matricula
	            WHERE id = :matricula_id;
            """

            dados = {
                "matricula_id": id
            }

            resultado = con.execute(text(sql), dados)

            if resultado.rowcount == 0:
                return {
                    "Matrícula não encontrada"
                }

            return {
                "Matrícula excluída com sucesso"
            }

    except Exception as e:
        return {
            "erro": str(e)
        }

    finally:
        engine.dispose()