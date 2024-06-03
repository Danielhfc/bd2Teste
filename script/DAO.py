from sqlalchemy.orm import Session
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from mapeamento import *

class DAO():
    # Conexão com o banco
    def getSession():
        engine = create_engine("postgresql+psycopg2://postgres:1234@localhost:5432/ticketmaster")
        Session = sessionmaker(bind=engine)
        session = Session()
        return session

    # Função de inserção no banco
    def insert(session, obj):
        session.add(obj)

# Funções para buscar um registro do banco
class DAOClassifications():
    
    def select(session, id):
        clas = session.query(Classification).filter(Classification.id == id).first()
        return clas

class DAOVenues():
    
    def select(session, id):
        loc = session.query(Venue).filter(Venue.id == id).first()
        return loc

class DAOEvents():
    
    def select(session, id):
        event = session.query(Event).filter(Event.id == id).first()
        return event

class DAOAttractions():

    def select(session, id):
        attraction = session.query(Attraction).filter(Attraction.id == id).first()
        return attraction
    
class DAOEventAttraction():

    def select(session, id):
        eventAttraction = session.query(eventAttraction).filter(eventAttraction.id == id).first()
        return eventAttraction

