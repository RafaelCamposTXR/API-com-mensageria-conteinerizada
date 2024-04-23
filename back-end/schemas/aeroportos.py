from pydantic import BaseModel

class AeroportosSchema(BaseModel):    
    nome: str
    cidade: str
    estado: str