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
    def selectClassification(id):
        try:
            session = DAO.getSession()
            session.expire_on_commit = False
            clas = DAOClassifications.select(session, id)
            session.commit()
            return clas
        except:
            return 0

    def selectVenue(id):
        try:
            session = DAO.getSession()
            session.expire_on_commit = False
            clas = DAOVenues.select(session, id)
            session.commit()
            return clas
        except:
            return 0

    def selectEvent(id):
        try:
            session = DAO.getSession()
            session.expire_on_commit = False
            clas = DAOEvents.select(session, id)
            session.commit()
            return clas
        except:
            return 0
        
    def selectAttraction(id):
        try:
            session = DAO.getSession()
            session.expire_on_commit = False
            org = DAOAttractions.select(session, id)
            session.commit()
            return org
        except:
            return 0
    
    def selectEventAttraction(id):
        try:
            session = DAO.getSession()
            session.expire_on_commit = False
            org = DAOEventAttraction.select(session, id)
            session.commit()
            return org
        except:
            return 0
    
class API:
    def __init__(self):
        self.manipulateDB = AcessDB


    def getClassifications(self):
        try:
            print('Fazendo a carga das classificações no banco...')
            response = requests.get("https://app.ticketmaster.com/discovery/v2/classifications.json?apikey=HvPlPVQ2sP3kTGbG19RGHGl9sQFvUNZX&page=0")
            classification_json = response.json()
            
            if len(classification_json) == 0:
                raise Exception('Json vazio')
            
            for clas in classification_json["_embedded"]["classifications"]:
                if 'segment' in clas:
                    segment_id = clas['segment']['id']
                    segment_nome = clas['segment']['name']

                    for genres in clas['segment']["_embedded"]['genres']:
                        
                        clasObject = Classification(genreid=genres['id'],
                                                genre=genres['name'],
                                                segmentid=str(segment_id),
                                                segmentname=str(segment_nome)
                                            )
                        
                         #Verifica se o objeto já existe no banco
                        check = self.manipulateDB.selectClassification(clasObject.genreid)
                        id = str(clasObject.genreid)
                        #Se não existir, insere no banco
                        if not check:
                            self.manipulateDB.insert(clasObject)
                            print('Classification inserida no banco. ID: ' + id)
                        else:
                            print('Classification já existe no banco. ID: ' + id)
                    
                elif 'type' in clas:
                    segment_id = clas['type']['id']
                    segment_nome = clas['type']['name']

                    for genres in clas['type']["_embedded"]['subtypes']:
                        
                        clasObject = Classification(genreid=genres['id'],
                                                genre=genres['name'],
                                                segmentid=str(segment_id),
                                                segmentnome=str(segment_nome)
                                            )
                        
                         #Verifica se o objeto já existe no banco
                        check = self.manipulateDB.selectClassificacao(clasObject.genreid)
                        id = str(clasObject.genreid)
                        #Se não existir, insere no banco
                        if not check:
                            self.manipulateDB.insert(clasObject)
                            print('Classificacao inserida no banco. ID: ' + id)
                        else:
                            print('Classificacao já existe no banco. ID: ' + id)
                    
               
            return 1

        except Exception as e:
            return '\nERRO: ' + repr(e)
        
    def getVenues(self):
        try:
            print('Fazendo a carga das Venues no banco...')
            for page in range(0,382):
                url = f"https://app.ticketmaster.com/discovery/v2/venues.json?apikey=HvPlPVQ2sP3kTGbG19RGHGl9sQFvUNZX&page={page}&size=200"
                response = requests.get(url)
                venues_json = response.json()
            
                if len(venues_json) == 0:
                    raise Exception('Json vazio')

                for ven in venues_json["_embedded"]["venues"]:

                    ven_aliases = ven['aliases'][0] if 'aliases' in ven and len(ven['aliases']) > 0 else None
                    ven_url = ven['url'] if 'url' in ven else None
                    ven_images = ven['images'][0]['url'] if 'images' in ven and len(ven['images']) > 0 else None
                    ven_market = ven['markets'][0]['name'] if 'markets' in ven and len(ven['markets']) > 0 else None
                    ven_address = ven['address']['line1'] if 'address' in ven and len(ven['address']) > 0 and 'line1' in ven['address'] else None

                    venObject = Venue(id=ven['id'],
                                            name=ven['name'],
                                            aliases=ven_aliases,
                                            url=ven_url,
                                            images=ven_images,
                                            postalcode=ven['postalCode'],
                                            timezone=ven['timezone'],
                                            cidade=ven['city']['name'],
                                            estado=ven['state']['name'],
                                            pais=ven['country']['name'],
                                            address=ven_address,
                                            market=ven_market,
                                        )
                    
                    #Verifica se o objeto já existe no banco
                    check = self.manipulateDB.selectVenue(venObject.id)
                    id = str(venObject.id)
                    #Se não existir, insere no banco
                    if not check:
                        self.manipulateDB.insert(venObject)
                        print('Venue inserido no banco. ID: ' + id)
                    else:
                        print('Venue já existe no banco. ID: ' + id)
            return 1

        except Exception as e:
            return '\nERRO: ' + repr(e)
        
    def getEvents(self):
        try:
            print('Fazendo a carga dos Events no banco...')
            for page in range(0,382):
                url = f"https://app.ticketmaster.com/discovery/v2/events.json?apikey=HvPlPVQ2sP3kTGbG19RGHGl9sQFvUNZX&page={page}&size=200"
                response = requests.get(url)
                events_json = response.json()
                
                if len(events_json) == 0:
                    raise Exception('Json vazio')

                for event in events_json["_embedded"]["events"]:
        
                    event_url = event['url'] if 'url' in event else None
                    event_images = event['images'][0]['url'] if 'images' in event and len(event['images']) > 0 else None
                    event_startDate = event['sales']['public']['startDateTime'] if 'startDateTime' in event['sales']['public'] else None
                    event_endDate = event['sales']['public']['endDateTime'] if 'endDateTime' in event['sales']['public'] else None
                    event_timezone = event['dates']['timezone'] if 'timezone' in event['dates'] else None
                    event_promoter = event['promoter']['name'] if 'promoter' in event else None
                    event_min = event['priceRanges'][0].get('min') if 'priceRanges' in event and len(event['priceRanges']) > 0 and 'min' in event['priceRanges'][0] else None
                    event_max = event['priceRanges'][0].get('max') if 'priceRanges' in event and len(event['priceRanges']) > 0 and 'max' in event['priceRanges'][0] else None
                    event_dateTime = event['dates']['start']['dateTime'] if 'dates' in event and 'start' in event['dates'] and 'dateTime' in event['dates']['start'] else None

                    eventObject = Event(id=event['id'],
                                            name=event['name'],
                                            url=event_url,
                                            images=event_images,
                                            startdatesale=event_startDate,
                                            enddatesale=event_endDate,
                                            startdateevent=event_dateTime,
                                            timezone=event_timezone,
                                            pricemin=event_min,
                                            pricemax=event_max,
                                            promoter=event_promoter,
                                            venue_id=event['_embedded']['venues'][0]['id'],
                                            classifications_id=event['classifications'][0]['genre']['id'],
                                        )

                    
                    #Verifica se o objeto já existe no banco
                    check = self.manipulateDB.selectEvent(eventObject.id)
                    id = str(eventObject.id)
                    #Se não existir, insere no banco
                    if not check:
                        self.manipulateDB.insert(eventObject)
                        print('Event inserido no banco. ID: ' + id)
                    else:
                        print('Event já existe no banco. ID: ' + id)
            return 1

        except Exception as e:
            return '\nERRO: ' + repr(e)
        
    def getAttractions(self):
        try:
            print('Fazendo a carga dos Attractions no banco...')
            for page in range(0,382):
                url = f"https://app.ticketmaster.com/discovery/v2/attractions.json?apikey=HvPlPVQ2sP3kTGbG19RGHGl9sQFvUNZX&page={page}&size=200"
                response = requests.get(url)
                attractions_json = response.json()
                
                if len(attractions_json) == 0:
                    raise Exception('Json vazio')

                for attr in attractions_json["_embedded"]["attractions"]:

                    attrObject = Attraction(id=attr['id'],
                                            name=attr['name'],
                                            url=attr['url'],
                                            images=attr['images'][0]['url'],
                                            classifications_id=attr['classifications'][0]['genre']['id'],
                                        )
                    
                    #Verifica se o objeto já existe no banco
                    check = self.manipulateDB.selectAttraction(attrObject.id)
                    id = str(attrObject.id)
                    #Se não existir, insere no banco
                    if not check:
                        self.manipulateDB.insert(attrObject)
                        print('Attraction inserido no banco. ID: ' + id)
                    else:
                        print('Attraction já existe no banco. ID: ' + id)
            return 1

        except Exception as e:
            return '\nERRO: ' + repr(e)