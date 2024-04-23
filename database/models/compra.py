from sqlalchemy import String, Integer, Column, TIMESTAMP, text, ForeignKey, DateTime
from .database import Base
from .voo import Voos


class Compras(Base):
    __tablename__ = 'compras'

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_voo = Column(ForeignKey(Voos.id)) 
    data_compra = Column(DateTime, default=DateTime.now()) 
    added_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('Now()'))