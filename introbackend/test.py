from fastapi import FastAPI
from sqlmodel import Session , select
from contextlib import asynccontextmanager
from database import create_db_and_tables, engine

from models import Retail, Crew, Order

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)



@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/Retail/{id}")
async def read_retail(id):
    with Session(engine) as session:
        print(id,'--------------------------------------------------------------')
        emp = session.get(Retail, id)
        return {"message": emp}
    

@app.post("/Retail")
async def root(retail : Retail):
    with Session(engine) as session:
        session.add(retail)
        session.commit()
        session.refresh(retail)

        return {"message": 'created'}

@app.get("/Crew/{id}")
async def read_crew(id):
    with Session(engine) as session:
        print(id,'--------------------------------------------------------------')
        emp = session.get(Crew, id)
        return {"message": emp}
    

@app.post("/Crew")
async def root(crew : Crew):
    with Session(engine) as session:
        session.add(crew)
        session.commit()
        session.refresh(crew)

        return {"message": 'created'}

@app.get("/Order/{id}")
async def read_order(id):
    with Session(engine) as session:
        print(id,'--------------------------------------------------------------')
        emp = session.get(order, id)
        return {"message": order}
    

@app.post("/Order")
async def root(order : Order):
    with Session(engine) as session:
        session.add(order)
        session.commit()
        session.refresh(order)

        return {"message": 'created'}