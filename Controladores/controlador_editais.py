from fastapi import APIRouter
from Classes._edital import Edital
from dotenv import load_dotenv
import os

load_dotenv()

#pip install sqlalchemy
from sqlalchemy import create_engine, text
router = APIRouter(prefix="/editais", tags=["Editais"])

#inserção no banco "postgresql://usuario:senha@servidor:porta/banco"
DATABASE_URL = os.getenv("DATABASE_URL")
#REST
#Create
@router.post('/cadastro') #Cadastro Edital
def cadastrar(edital: Edital):

    engine = create_engine(DATABASE_URL)

    try:
        with engine.begin() as con:

            sql = """
                INSERT INTO public.edital(
	                nome, descricao, banca, data_cadastro, data_prova, ativo)
	            VALUES (:nome, :descricao, :banca, :data_cadastro, :data_prova, :ativo);
            """

            dados = {
                "nome": edital.nome,
                "descricao": edital.descricao,
                "banca": edital.banca,
                "data_cadastro": edital.data_cadastro,
                "data_prova": edital.data_prova,
                "ativo": edital.ativo,
                
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
	            SET nome=:nome, descricao=:descricao, banca=:banca, data_cadastro=:data_cadastro, data_prova=:data_prova, ativo=:ativo
	            WHERE id = :id;
            """

            dados = {
                "id": id,
                "nome": edital.nome,
                "descricao": edital.descricao,
                "banca": edital.banca,
                "data_cadastro": edital.data_cadastro,
                "data_prova": edital.data_prova,
                "ativo": edital.ativo,
                
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
