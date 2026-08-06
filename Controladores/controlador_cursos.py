from fastapi import APIRouter
from Classes._curso import Curso


#pip install sqlalchemy
from sqlalchemy import create_engine, text
router = APIRouter(prefix="/cursos", tags=["cursos"])

#inserção no banco "postgresql://usuario:senha@servidor:porta/banco"
# Altere esta linha no controlador_usuario.py:
DATABASE_URL = "postgresql://postgres:123@localhost:5432/Zap"
#REST
#Create
@router.post('/cadastro')
def cadastrar(curso: Curso):

    engine = create_engine(DATABASE_URL)

    try:
        with engine.begin() as con:

            sql = """
                INSERT INTO public.curso(
	            nome, descricao, carga_horaria, valor, inicio_aulas, ativo)
	            VALUES (:nome, :descricao, :carga_horaria, :valor, :inicio_aulas, :ativo);
            """

            dados = {
                "nome": curso.nome,
                "descricao": curso.descricao,
                "carga_horaria": curso.carga_horaria,
                "valor": curso.valor,
                "inicio_aulas": curso.inicio_aulas,
                "ativo": curso.ativo
            }

            con.execute(text(sql), dados)

            return {
                "mensagem": "Curso cadastrado com sucesso"
            }

    except Exception as e:
        print(repr(e)) # Printa o erro cru no terminal do VS Code
        return {
            "erro": str(e)
        }

    finally:
        engine.dispose()


@router.put('/{id}')
def atualizar(id: int, curso: Curso):

    engine = create_engine(DATABASE_URL)

    try:
        with engine.begin() as con:

            sql = """
                UPDATE public.curso
	            SET id=:id, nome=:nome, descricao=:descricao, carga_horaria=:carga_horaria, valor=:valor, inicio_aulas=:inicio_aulas, ativo=:ativo
	            WHERE id = :id;
            """

            dados = {
                "id": id,
                "nome": curso.nome,
                "descricao": curso.descricao,
                "carga_horaria": curso.carga_horaria,
                "valor": curso.valor,
                "inicio_aulas": curso.inicio_aulas,
                "ativo": curso.ativo
            }

            resultado = con.execute(text(sql), dados)

            if resultado.rowcount == 0:
                return {
                    "Curso não encontrado"
                }

            return {
                "Curso atualizado com sucesso"
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
                DELETE FROM public.curso
	            WHERE id = :id;
            """

            dados = {
                "id": id
            }

            resultado = con.execute(text(sql), dados)

            if resultado.rowcount == 0:
                return {
                    "Curso não encontrado"
                }

            return {
                "Curso excluído com sucesso"
            }

    except Exception as e:
        return {
            "erro": str(e)
        }

    finally:
        engine.dispose()