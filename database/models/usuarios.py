from sqlalchemy import String, Integer, Column, TIMESTAMP, text
from .database import Base

class Usuarios(Base):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(50), nullable=False)
    email = Column(String(20), nullable=False)
    senha = Column(String(40), nullable=False)         
    added_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('Now()'))