from sqlalchemy import Column, Integer, String, DECIMAL
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel
from typing import Optional
from decimal import Decimal

Base = declarative_base()

class Cerveja(Base):
    __tablename__ = "cerveja"
    
    id_cerveja = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    estoque = Column(Integer, default=0)  
    valor = Column(DECIMAL(10, 5), nullable=False)

class CervejaBase(BaseModel):
    id_cerveja: Optional[int]
    nome: str
    estoque: Optional[int]
    valor: Decimal

    class Config:
        from_attributes = True

class CervejaIn(BaseModel):  
    nome: str
    estoque: Optional[int] = 0
    valor: Decimal

    class Config:
        from_attributes = True
