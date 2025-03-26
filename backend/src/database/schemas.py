from sqlalchemy import Column, Integer, String, DATETIME

from src.database.main import Base


class OperadoraBase(Base):
    __tablename__ = "operadoras"

    id = Column(Integer, primary_key=True, index=True)
    registro_ans = Column(String, index=True)
    cnpj = Column(String, index=True)
    razao_social = Column(String, index=True)
    nome_fantasia = Column(String, index=True, nullable=True)
    modalidade = Column(String, index=True, nullable=True)
    logradouro = Column(String, index=True)
    numero = Column(String, index=True)
    complemento = Column(String, index=True, nullable=True)
    bairro = Column(String, index=True)
    cidade = Column(String, index=True)
    uf = Column(String, index=True)
    cep = Column(String, index=True)
    ddd = Column(String, index=True, nullable=True)
    telefone = Column(String, index=True, nullable=True)
    fax = Column(String, index=True, nullable=True)
    email = Column(String, index=True, nullable=True)
    representante_legal = Column(String, index=True)
    cargo_representante = Column(String, index=True)
    regiao_operacao = Column(Integer, index=True, nullable=True)
    data_registro = Column(DATETIME, index=True, nullable=True)

    def __repr__(self):
        return f"<OperadoraBase(reg_ans={self.reg_ans}, cnpj={self.cnpj}, razao_social={self.razao_social}, nome_fantasia={self.nome_fantasia}, modalidade={self.modalidade}, logradouro={self.logradouro}, numero={self.numero}, complemento={self.complemento}, bairro={self.bairro}, cidade={self.cidade}, uf={self.uf}, cep={self.cep}, ddd={self.ddd}, telefone={self.telefone}, fax={self.fax}, email={self.email}, representante_legal={self.representante_legal}, cargo_representante={self.cargo_representante}, regiao_operacao={self.regiao_operacao}, data_registro={self.data_registro})>"