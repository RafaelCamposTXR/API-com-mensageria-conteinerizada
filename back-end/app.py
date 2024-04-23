from fastapi import FastAPI
from typing import Optional
from routers.voos import router as router_lista_aeroportos
#from mensageria.rabbitmq import connect, canal

app = FastAPI()
app.include_router(router_lista_aeroportos)

@app.get("/")
async def hello():
  return {"Aiai viu"}