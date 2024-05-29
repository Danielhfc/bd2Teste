from sqlalchemy.orm import Session
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from mapeamento import *

class DAO():
    # Conexão com o banco
    def getSession():
        engine = create_engine("postgresql+psycopg2://postgres:1234@localhost:5432/ticketnaster")
        Session = sessionmaker(bind=engine)
        session = Session()
        return session

    # Função de inserção no banco
    def insert(session, obj):
        session.add(obj)

# Funções para buscar um registro do banco
class DAOClassificacoes():
    
    def select(session, id):
        clas = session.query(Classificacao).filter(Classificacao.id == id).first()
        return clas

class DAOLocais():
    
    def select(session, id):
        loc = session.query(Locais).filter(Locais.id == id).first()
        return loc

class DAOEventos():
    
    def select(session, id):
        event = session.query(Evento).filter(Evento.id == id).first()
        return event

class DAOAtracoes():

    def select(session, id):
        atrac = session.query(Atracao).filter(Atracao.id == id).first()
        return atrac

