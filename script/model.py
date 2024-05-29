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
    
