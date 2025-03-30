import csv
import os
from datetime import datetime

from fastapi import FastAPI, HTTPException
from src.database.main import SessionLocal
from src.database.schemas import OperadoraBase
from fastapi.middleware.cors import CORSMiddleware

from src.models.operadoras import Operadora

mock_data: list[Operadora] = []

file_path = os.path.join(os.path.dirname(__file__), "mock.csv")

with open(file_path, mode="r", encoding="utf-8") as file:
    reader = csv.reader(file, delimiter=';')
    next(reader)
    for row in reader:
        data_registro = None
        if row[19]:
            try:
                data_registro = datetime.strptime(row[19], "%d/%m/%Y").date()
            except ValueError:
                data_registro = datetime.strptime(row[19], "%Y-%m-%d").date()
        mock_data.append(
            Operadora(
                id=int(row[0]),
                registro_ans=row[1],
                cnpj=row[1],
                razao_social=row[2],
                nome_fantasia=row[3],
                modalidade=row[4],
                logradouro=row[5],
                numero=row[6],
                complemento=row[7],
                bairro=row[8],
                cidade=row[9],
                uf=row[10],
                cep=row[11],
                telefone=f"{row[12]} {row[13]}",
                email=row[15],
                representante_legal=row[16],
                cargo_representante=row[17],
                regiao_operacao=int(row[18]) if row[18] else None,
                data_registro=data_registro,
            )
        )

app = FastAPI(
    title="Intuitive Care API",
    description="API to GET Orgs",
    version="0.1.0",
    contact={
        "name": "Caio Reis",
        "email": "caiodtn@gmail.com"
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
async def say_hello(name: str = None, mock: bool = False) -> list[Operadora]:
    if not name:
        raise HTTPException(status_code=400, detail="Name is required")

    if mock:
        org = [item for item in mock_data if name.lower() in item.nome_fantasia.lower()]
        if not org:
            raise HTTPException(status_code=404, detail="No organization found")
        return org

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
                    telefone=f"{item.ddd} {item.telefone}",
                    email=item.email,
                    representante_legal=item.representante_legal,
                    cargo_representante=item.cargo_representante,
                    regiao_operacao=item.regiao_operacao,
                    data_registro=item.data_registro
                )
            )
    db.close()
    return response
