# coding: utf-8
from sqlalchemy import Column, Date, Float, ForeignKey, Text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Classificacao(Base):
    __tablename__ = 'classificacao'

    id = Column(Text, primary_key=True)


class Locais(Base):
    __tablename__ = 'locais'

    id = Column(Text, primary_key=True)
    nome = Column(Text, nullable=False)
    codigourl = Column(Text)
    imagens = Column(Text, nullable=False)
    codigopostal = Column(Text, nullable=False)
    timezone = Column(Text, nullable=False)
    cidade = Column(Text, nullable=False)
    estado = Column(Text, nullable=False)
    pais = Column(Text, nullable=False)
    proximoseventos = Column(Text, nullable=False)


class Evento(Base):
    __tablename__ = 'eventos'

    id = Column(Text, primary_key=True)
    nome = Column(Text, nullable=False)
    codigourl = Column(Text)
    imagens = Column(Text, nullable=False)
    iniciovenda = Column(Date, nullable=False)
    fimvenda = Column(Date, nullable=False)
    inicioevento = Column(Date, nullable=False)
    fimevento = Column(Date, nullable=False)
    preco = Column(Float(53), nullable=False)
    local_id = Column(ForeignKey('locais.id'))
    classificacao_id = Column(ForeignKey('classificacao.id'))

    classificacao = relationship('Classificacao')
    local = relationship('Locais')


class Atracao(Base):
    __tablename__ = 'atracoes'

    id = Column(Text, primary_key=True)
    nome = Column(Text, nullable=False)
    codigourl = Column(Text)
    imagens = Column(Text, nullable=False)
    proximoseventos = Column(Text, nullable=False)
    classificacao_id = Column(ForeignKey('classificacao.id'))
    evento_id = Column(ForeignKey('eventos.id'))

    classificacao = relationship('Classificacao')
    evento = relationship('Evento')
