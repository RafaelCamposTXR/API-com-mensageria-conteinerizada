from fastapi import FastAPI
from typing import Optional
from routers.alunos import router as router_alunos

app = FastAPI()
app.include_router(router_alunos)

