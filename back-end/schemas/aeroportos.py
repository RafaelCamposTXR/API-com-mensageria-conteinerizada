from pydantic import BaseModel

class Aeroporto(BaseModel):
    code: str
    name: str
    city: str
    country: str