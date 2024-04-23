from fastapi import FastAPI
from typing import Optional
from routers.voos import router as router_lista_aeroportos
<<<<<<< Updated upstream
#from routers.aeroportos import router as aeroportos_router
#from mensageria.rabbitmq import connect, canal
=======
from mensageria.rabbitmq import connect, canal
>>>>>>> Stashed changes

app = FastAPI()
app.include_router(router_lista_aeroportos)
#app.include_router(aeroportos_router)

@app.get("/")
async def hello():
  return {"Aiai viu"}