from fastapi import FastAPI, HTTPException
from src.database.main import SessionLocal
from src.database.schemas import OperadoraBase
from fastapi.middleware.cors import CORSMiddleware

from src.models.operadoras import Operadora


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


@app.get("/search", response_model_exclude_none=True, response_model=list[Operadora])
async def say_hello(name: str = None):
    if not name:
        raise HTTPException(status_code=400, detail="Name is required")

    with SessionLocal() as db:
        org = db.query(OperadoraBase).filter(
            (OperadoraBase.razao_social.like(f"%{name}%")) |
            (OperadoraBase.nome_fantasia.like(f"%{name}%"))
        ).all()
        if not org:
            raise HTTPException(status_code=404, detail="No organization found")

        response: list[Operadora] = []

        for item in org:
            response.append(
                Operadora(
                    id=item.id,
                    registro_ans=item.registro_ans,
                    cnpj=item.cnpj,
                    razao_social=item.razao_social,
                    nome_fantasia=item.nome_fantasia,
                    modalidade=item.modalidade,
                    cep=item.cep,
                    logradouro=item.logradouro,
                    numero=item.numero,
                    complemento=item.complemento,
                    bairro=item.bairro,
                    cidade=item.cidade,
                    uf=item.uf,
                    telefone=item.telefone,
                    email=item.email,
                    representante_legal=item.representante_legal,
                    cargo_representante=item.cargo_representante,
                    regiao_operacao=item.regiao_operacao,
                    data_registro=item.data_registro
                )
            )
    db.close()
    return response
