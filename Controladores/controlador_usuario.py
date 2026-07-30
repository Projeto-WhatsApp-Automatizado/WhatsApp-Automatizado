from fastapi import APIRouter
from _usuario import Usuario


#pip install sqlalchemy
from sqlalchemy import create_engine, text
router = APIRouter(prefix="/usuarios", tags=["usuarios"])

#inserção no banco "postgresql://usuario:senha@servidor:porta/banco"
DATABASE_URL = "postgresql://postgres:123@localhost:5432/Zap?client_encoding=win1252"
#REST
#Create
@router.post('/cadastro')
def cadastrar(usuario: Usuario):

    engine = create_engine(DATABASE_URL)

    try:
        with engine.begin() as con:

            sql = """
                INSERT INTO public.usuario(
	                nome, email, telefone, estado, interesse)
	            VALUES (:usu_nome, :usu_email, :usu_telefone, :usu_estado, :usu_interesse);
            """

            dados = {
                "usu_nome": usuario.nome,
                "usu_email": usuario.email,
                "usu_telefone": usuario.telefone,
                "usu_estado": usuario.estado,
                "usu_interesse": usuario.interesse
            }

            con.execute(text(sql), dados)

            return {
                "mensagem": "Usuário cadastrado com sucesso"
            }

    except Exception as e:
        print(repr(e)) # Printa o erro cru no terminal do VS Code
        return {
            "erro": str(e)
        }

    finally:
        engine.dispose()


@router.put('/{id}')
def atualizar(id: int, usuario: Usuario):

    engine = create_engine(DATABASE_URL)

    try:
        with engine.begin() as con:

            sql = """
                UPDATE public.usuario
	            SET nome=:usu_nome, email=:usu_email, telefone=:usu_telefone, estado=:usu_estado, interesse=:usu_interesse
	            WHERE id = :usu_id;
            """

            dados = {
                "usu_id": id,
                "usu_nome": usuario.nome,
                "usu_email": usuario.email,
                "usu_telefone": usuario.telefone,
                "usu_estado": usuario.estado,
                "usu_interesse": usuario.interesse
            }

            resultado = con.execute(text(sql), dados)

            if resultado.rowcount == 0:
                return {
                    "Usuário não encontrado"
                }

            return {
                "Usuário atualizado com sucesso"
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
                DELETE FROM public.usuario
	            WHERE id = :usu_id;
            """

            dados = {
                "usu_id": id
            }

            resultado = con.execute(text(sql), dados)

            if resultado.rowcount == 0:
                return {
                    "Usuário não encontrado"
                }

            return {
                "Usuário excluído com sucesso"
            }

    except Exception as e:
        return {
            "erro": str(e)
        }

    finally:
        engine.dispose()