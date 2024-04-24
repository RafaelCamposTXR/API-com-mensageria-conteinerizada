from pydantic import BaseModel
from sqlalchemy import DateTime
from typing import Optional

class AeroportosSchema(BaseModel):    
    nome: str
    cidade: str
    estado: str

class ComprasSchema(BaseModel):    
    id_voo: int 
    data_compra: str

class UsuariosSchema(BaseModel):    
    nome: str
    email: str
    senha: str

class VoosSchema(BaseModel):    
    aeroporto_saida: int 
    aeroporto_chegada: int
    data_saida: str
    data_chegada: str
    preco: float

class Operation(BaseModel):
    id: int
    origem: Optional[str] = None
    data: Optional[str] = None
    passageiros: Optional[int] = None