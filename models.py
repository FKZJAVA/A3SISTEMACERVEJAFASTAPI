from sqlalchemy import Column, Integer, String, ForeignKey, DECIMAL, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from pydantic import BaseModel
from typing import Optional, List
from decimal import Decimal

Base = declarative_base()


class Cerveja(Base):
    __tablename__ = "cerveja"
    
    id_cerveja = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    estoque = Column(Integer, default=0)  
    valor = Column(DECIMAL(10, 5), nullable=False)
    
    detalhes_pedidos = relationship("DetalhesPedidos", back_populates="cerveja")



class Pedido(Base):
    __tablename__ = "pedido"
    
    id_pedido = Column(Integer, primary_key=True, index=True)
    cliente_nome = Column(String(100), nullable=False)
    data_pedido = Column(DateTime, default=datetime.utcnow)
    
    detalhes_pedidos = relationship("DetalhesPedidos", back_populates="pedido")



class DetalhesPedidos(Base):
    __tablename__ = "detalhes_pedidos"
    
    id_pedido = Column(Integer, ForeignKey("pedido.id_pedido"), primary_key=True)
    id_cerveja = Column(Integer, ForeignKey("cerveja.id_cerveja"), primary_key=True)
    quantidade = Column(Integer, nullable=False)
    total = Column(DECIMAL(10, 5), nullable=False)
    
    pedido = relationship("Pedido", back_populates="detalhes_pedidos")
    cerveja = relationship("Cerveja", back_populates="detalhes_pedidos")

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



class PedidoBase(BaseModel):
    id_pedido: Optional[int]
    cliente_nome: str
    data_pedido: datetime

    class Config:
        from_attributes = True


class PedidoIn(BaseModel):  
    cliente_nome: str

    class Config:
        from_attributes = True



class DetalhesPedidosBase(BaseModel):
    id_pedido: int
    id_cerveja: int
    quantidade: int
    total: Decimal

    class Config:
        from_attributes = True


class DetalhesPedidosIn(BaseModel):  
    id_cerveja: int
    quantidade: int
    total: Decimal

    class Config:
        from_attributes = True