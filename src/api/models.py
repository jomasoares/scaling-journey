from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base

class Corretor(Base):
    __tablename__ = "corretores"

    corretorId = Column(String, primary_key=True, index=True, name="corretor_id")
    cpfCnpj = Column(String, name="cpf_cnpf")
    protocolo = Column(String)
    nome = Column(String)
    recadastrado = Column(Boolean)
    situacao = Column(String)
    produtos = Column(String)
    dataInsercao = Column(String, name="data_insercao") #TODO: mudar para timestamp?
