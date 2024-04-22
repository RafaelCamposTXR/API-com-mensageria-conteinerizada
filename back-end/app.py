from fastapi import FastAPI
from typing import Optional
from routers.lista_aeroportos import router as router_lista_aeroportos

app = FastAPI()
app.include_router(router_lista_aeroportos)

