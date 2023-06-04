from pydantic import BaseModel

class Corretor(BaseModel):
    corretorId: str
    cpfCnpj: str
    protocolo: str
    nome: str
    recadastrado: bool
    situacao: str
    produtos: str

    class Config:
        orm_mode = True

