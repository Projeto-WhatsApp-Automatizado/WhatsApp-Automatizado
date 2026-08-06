from fastapi import APIRouter
from Classes._edital import Edital


#pip install sqlalchemy
from sqlalchemy import create_engine, text
router = APIRouter(prefix="/edital", tags=["Edital"])

#inserção no banco "postgresql://usuario:senha@servidor:porta/banco"
DATABASE_URL = "postgresql://postgres:123@localhost:5432/Zap" #adicionar enderço do banco que iremos criar
#REST
#Create
@router.post('/cadastro') #Cadastro Edital
def cadastrar(edital: Edital):

    engine = create_engine(DATABASE_URL)

    try:
        with engine.begin() as con:

            sql = """
                INSERT INTO public.edital(
	            nome, descricao, data_prova, data_cadastro, status, banca)
	            VALUES (:nome, :descricao, :data_prova, :data_cadastro, :status, :banca);
            """

            dados = {
                "nome": edital.nome,
                "descricao": edital.descricao,
                "data_prova": edital.data_prova,
                "data_cadastro": edital.data_cadastro,
                "status": edital.status,
                "banca": edital.banca
            }

            con.execute(text(sql), dados)

            return {
                "mensagem": "Edital cadastrado com sucesso"
            }

    except Exception as e:
        return {
            "erro": str(e)
        }

    finally:
        engine.dispose()     
 

       
@router.put('/{id}') #Atualizar Edital 
def atualizar(id: int, edital: Edital):

    engine = create_engine(DATABASE_URL)

    try:
        with engine.begin() as con:

            sql = """
                UPDATE public.edital
                SET nome = :nome,
                    descricao = :descricao,
                    data_prova = :data_prova,
                    data_cadastro = :data_cadastro,
                    status = :status,
                    banca = :banca
                WHERE id = :id
            """

            dados = {
                "id": id,
                "nome": edital.nome,
                "descricao": edital.descricao,
                "data_prova": edital.data_prova,
                "data_cadastro": edital.data_cadastro,
                "status": edital.status,
                "banca": edital.banca
            }

            resultado = con.execute(text(sql), dados)

            if resultado.rowcount == 0:
                return {
                    "mensagem": "Cliente não encontrado"
                }

            return {
                "mensagem": "Edital atualizado com sucesso"
            }

    except Exception as e:
        return {
            "erro": str(e)
        }

    finally:
        engine.dispose()

@router.delete('/{id}') #Deletar Edital
def deletar(id: int):

    engine = create_engine(DATABASE_URL)

    try:
        with engine.begin() as con:

            sql = """
                DELETE FROM public.edital
                WHERE id = :id
            """

            dados = {
                "id": id
            }

            resultado = con.execute(text(sql), dados)

            if resultado.rowcount == 0:
                return {
                    "mensagem": "Edital não encontrado"
                }

            return {
                "mensagem": "Edital excluído com sucesso"
            }

    except Exception as e:
        return {
            "erro": str(e)
        }

    finally:
        engine.dispose()
