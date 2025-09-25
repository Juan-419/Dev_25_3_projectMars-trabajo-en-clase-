from fastapi import FastAPI

import appoinment
import pet
import estudiantes
import user
import vet
from db import create_tables
##from pet import APIRouter

app = FastAPI(lifespan=create_tables, title="Pet API")
app.include_router(pet.router, tags=["pet"], prefix="/pets")
app.include_router(user.router, tags=["user"], prefix="/users")
app.include_router(vet.router, tags=["vet"], prefix="/vets")
app.include_router(appoinment.router, tags=["appointment"], prefix="/appointments")
#app.include_router(estudiantes.router, tags=["estudiantes"], prefix="/estudiantes" )


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

