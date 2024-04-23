from pydantic import BaseModel
from sqlalchemy import DateTime

class ComprasSchema(BaseModel):    
    id_voo = int 
    data_compra = DateTime