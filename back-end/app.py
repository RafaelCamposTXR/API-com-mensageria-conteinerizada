from fastapi import FastAPI
from typing import Optional
#from routers.voos import router as router_lista_aeroportos
#from routers.aeroportos import router as router_aeroportos



app = FastAPI()
#app.include_router(router_lista_aeroportos)
#app.include_router(router_aeroportos)

@app.get("/")
async def hello():
  return {"Aiai viu"}