# coding: utf-8
from sqlalchemy.orm import Session
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import ObjectDeletedError
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.orm.exc import StaleDataError
import uuid
from DAO import *
from mapeamento import *

import json
import requests
from datetime import datetime

class AcessDB:
    # Função de inserção no banco
    def insert(obj):
        try:
            session = DAO.getSession()
            DAO.insert(session, obj)
            session.commit()
            session.close()
            return 1
        except Exception as e:
            print(e)
            session.close()
            return 0

    # Funções para buscar um registro do banco
    def selectClassificacao(id):
        try:
            session = DAO.getSession()
            session.expire_on_commit = False
            dep = DAOClassificacoes.select(session, id)
            session.commit()
            return dep
        except:
            return 0

    def selectLocal(id):
        try:
            session = DAO.getSession()
            session.expire_on_commit = False
            dep = DAOLocais.select(session, id)
            session.commit()
            return dep
        except:
            return 0

    def selectEvento(id):
        try:
            session = DAO.getSession()
            session.expire_on_commit = False
            dep = DAOEventos.select(session, id)
            session.commit()
            return dep
        except:
            return 0
        
    def selectAtracao(id):
        try:
            session = DAO.getSession()
            session.expire_on_commit = False
            org = DAOAtracoes.select(session, id)
            session.commit()
            return org
        except:
            return 0
    
class API:
    def __init__(self):
        self.manipulateDB = AcessDB

    def getClassificacoes(self):
        try:
            print('Fazendo a carga das classificações no banco...')
            response = requests.get("https://app.ticketmaster.com/discovery/v2/classifications.json?apikey=HvPlPVQ2sP3kTGbG19RGHGl9sQFvUNZX&page=0")
            classificacao_json = response.json()
            
            if len(classificacao_json) == 0:
                raise Exception('Json vazio')

            # Acessando a lista de classificações dentro do campo "_embedded"
            classifications = classificacao_json["_embedded"]["classifications"]
            
            for clas in classifications:
                # Verificando se 'segment' e 'type' estão presentes em 'clas'
                if 'segment' in clas:
                    # Acessando o segment id e imprimindo para verificar
                    segment_id = clas['segment']['id']
                    print(f"Segment ID: {segment_id}")
                    
                    clasObject = Classificacao(id=str(segment_id))
                    
                    # Verifica se o objeto já existe no banco
                    check = self.manipulateDB.selectClassificacao(clasObject.id)
                    id = str(clasObject.id)

                    # Se não existir, insere no banco
                    if not check:
                        self.manipulateDB.insert(clasObject)
                        print('Classificacao inserida no banco. ID: ' + id)
                    else:
                        print('Classificacao já existe no banco. ID: ' + id)
                else:
                    # Acessando o segment id e imprimindo para verificar
                    segment_id = clas['type']['id']
                    print(f"Segment ID: {segment_id}")
                    
                    clasObject = Classificacao(id=str(segment_id))
                    
                    # Verifica se o objeto já existe no banco
                    check = self.manipulateDB.selectClassificacao(clasObject.id)
                    id = str(clasObject.id)

                    # Se não existir, insere no banco
                    if not check:
                        self.manipulateDB.insert(clasObject)
                        print('Classificacao inserida no banco. ID: ' + id)
                    else:
                        print('Classificacao já existe no banco. ID: ' + id)
            return 1

        except Exception as e:
            return '\nERRO: ' + repr(e)