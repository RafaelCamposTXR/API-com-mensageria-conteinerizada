from sqlalchemy import String, Integer, Column, TIMESTAMP, text, ForeignKey, DateTime, Float
from .database import Base
from .aeroporto import Aeroportos


class Voos(Base):
    __tablename__ = 'voos'

    id = Column(Integer, primary_key=True, autoincrement=True)
    aeroporto_saida = Column(ForeignKey(Aeroportos.id)) 
    aeroporto_chegada = Column(ForeignKey(Aeroportos.id))
    data_saida = Column(DateTime, nullable=False)
    data_chegada = Column(DateTime, nullable=False)
    preco = Column(Float, default=0)  
    added_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('Now()'))