from pydantic import BaseModel
from sqlalchemy import DateTime
class VoosSchema(BaseModel):    
    aeroporto_saida = int 
    aeroporto_chegada = int
    data_saida = DateTime
    data_chegada = DateTime
    preco = float