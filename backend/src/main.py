from fastapi import FastAPI
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session
from src.database.main import SessionLocal
from src.database.schemas import OperadoraBase
from fastapi.middleware.cors import CORSMiddleware

db: Session = SessionLocal()



app = FastAPI(
    title="Intuitive Care API",
    description="API to manage to GET Data from Intuitive Care Database",
    version="0.1.0",
    contact={
        "name": "Caio Reis",

    }
)

origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
async def root():
    return {"message": "Hello World"}


@app.get("/search")
async def say_hello(name: str = None):
    if not name:
        raise HTTPException(status_code=400, detail="Name is required")



    org = db.query(OperadoraBase).filter(
        (OperadoraBase.razao_social.like(f"%{name}%")) |
        (OperadoraBase.nome_fantasia.like(f"%{name}%"))
    ).all()
    if not org:
        db.close()
        raise HTTPException(status_code=404, detail="No organization found")

    db.close()
    return org