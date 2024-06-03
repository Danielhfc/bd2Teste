# coding: utf-8
from sqlalchemy import Column, Date, Float, ForeignKey, Integer, Text, text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Classification(Base):
    __tablename__ = 'classifications'

    genreid = Column(Text, primary_key=True)
    genre = Column(Text, nullable=False)
    segmentid = Column(Text, nullable=False)
    segmentname = Column(Text, nullable=False)


class Venue(Base):
    __tablename__ = 'venues'

    id = Column(Text, primary_key=True)
    name = Column(Text, nullable=False)
    aliases = Column(Text)
    url = Column(Text)
    images = Column(Text)
    postalcode = Column(Text, nullable=False)
    timezone = Column(Text, nullable=False)
    cidade = Column(Text, nullable=False)
    estado = Column(Text, nullable=False)
    pais = Column(Text, nullable=False)
    address = Column(Text, nullable=True)
    market = Column(Text)


class Attraction(Base):
    __tablename__ = 'attractions'

    id = Column(Text, primary_key=True)
    name = Column(Text, nullable=False)
    url = Column(Text)
    images = Column(Text, nullable=False)
    classifications_id = Column(ForeignKey('classifications.genreid'))

    classifications = relationship('Classification')


class Event(Base):
    __tablename__ = 'events'

    id = Column(Text, primary_key=True)
    name = Column(Text, nullable=False)
    url = Column(Text)
    images = Column(Text)
    startdatesale = Column(Date)
    enddatesale = Column(Date)
    startdateevent = Column(Date)
    timezone = Column(Text)
    pricemin = Column(Float(53))
    pricemax = Column(Float(53))
    promoter = Column(Text)
    venue_id = Column(ForeignKey('venues.id'))
    classifications_id = Column(ForeignKey('classifications.genreid'))

    classifications = relationship('Classification')
    venue = relationship('Venue')


class EventAttraction(Base):
    __tablename__ = 'event_attraction'

    id = Column(Integer, primary_key=True, server_default=text("nextval('event_attraction_id_seq'::regclass)"))
    attractions_id = Column(ForeignKey('attractions.id'), nullable=False)
    events_id = Column(ForeignKey('events.id'), nullable=False)

    attractions = relationship('Attraction')
    events = relationship('Event')
