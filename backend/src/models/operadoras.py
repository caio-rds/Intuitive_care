import datetime
from typing import Optional

from pydantic import BaseModel

class Operadora(BaseModel):
    id: int
    registro_ans: str
    cnpj: str
    razao_social: str
    nome_fantasia: Optional[str] = None
    modalidade: Optional[str] = None
    cep: str
    logradouro: str
    numero: str
    complemento: Optional[str] = None
    bairro: str
    cidade: str
    uf: str
    telefone: Optional[str] = None
    email: Optional[str] = None
    representante_legal: str
    cargo_representante: str
    regiao_operacao: Optional[int] = None
    data_registro: Optional[datetime.date] = None
