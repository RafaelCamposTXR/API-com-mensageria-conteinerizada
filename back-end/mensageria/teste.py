from models.schemas import Operation
from fastapi import FastAPI, APIRouter, Depends, HTTPException
import json


nome = Operation(id= 0)


dados_json = nome.model_dump_json()



