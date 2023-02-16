"""
Models definitions to create database
"""
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from erer_dashboard.infra.base_model import Base

class Lote(Base):
    """
    Model of LOTE
    Represente a input proccess of a file
    """
    __tablename__ = "lote"

    id          : int        = Column(Integer, primary_key=True, index=True, autoincrement=True)
    file_name   : String     = Column(String)
    ano_ref     : int        = Column(Integer)
    processedAt : datetime   = Column(DateTime, default=datetime.now)
