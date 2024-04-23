from sqlalchemy import String, Integer, Column, TIMESTAMP, text
from .database import Base

class Aeroportos(Base):
    __tablename__ = 'aeroportos'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(50), nullable=False)     
    cidade = Column(String(40), nullable=False)
    estado = Column(String(2), nullable=False)    
    added_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('Now()'))