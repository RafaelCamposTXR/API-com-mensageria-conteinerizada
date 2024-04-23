from pydantic import BaseModel

class UsuariosSchema(BaseModel):    
    nome: str
    email: str
    senha: str