from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, TIMESTAMP, text, DateTime, Float
from sqlalchemy.orm import relationship
from models.database import Base

class Aeroportos(Base):
    __tablename__ = 'aeroportos'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(50), nullable=False)     
    cidade = Column(String(40), nullable=False)
    estado = Column(String(2), nullable=False)    
    added_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('Now()'))
class Voos(Base):
    __tablename__ = 'voos'

    id = Column(Integer, primary_key=True, autoincrement=True)
    aeroporto_saida = Column(ForeignKey(Aeroportos.id)) 
    aeroporto_chegada = Column(ForeignKey(Aeroportos.id))
    data_saida = Column(DateTime, nullable=False)
    data_chegada = Column(DateTime, nullable=False)
    preco = Column(Float, default=0)  
    added_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('Now()'))

class Compras(Base):
    __tablename__ = 'compras'

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_voo = Column(ForeignKey(Voos.id)) 
    data_compra = Column(DateTime, default=DateTime.now()) 
    added_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('Now()'))

class Usuarios(Base):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(50), nullable=False)
    email = Column(String(20), nullable=False)
    senha = Column(String(40), nullable=False)         
    added_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('Now()'))

