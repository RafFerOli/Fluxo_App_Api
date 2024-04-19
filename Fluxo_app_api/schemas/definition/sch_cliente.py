from pydantic import BaseModel
from typing import Optional, List
from model.table.tb_cliente import Cliente

from schemas import NotaSchema

class ClienteSchema(BaseModel):
    """ Define como um novo cliente a ser inserido deve ser representado
    """
    nome: str = "Zézinho"
    descricao: Optional[str] = "Produtor de bolinhas"
    cnpj: str = "12.345.678.0001/90"


class ClienteBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no nome do cliente.
    """
    nome: str = "Zé"


class ListagemClientesSchema(BaseModel):
    """ Define como uma listagem de clientes será retornada.
    """
    clientes:List[ClienteSchema]


class ClienteViewSchema(BaseModel):
    """ Define como um cliente será retornado: cliente + notas.
    """
    id: int = 1
    nome: str = "Zézinho ltda"
    descricao: Optional[str] = "Produtora de bolinhas"
    cnpj: str = "12.345.678.0001/90"
    total_notas: int = 1
    notas:List[NotaSchema]


class ClienteDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    mesage: str
    nome: str


def apresenta_cliente(cliente: Cliente):
    """ Retorna uma representação do cliente seguindo o schema definido em
        ClienteViewSchema.
    """
    return {
        "id": cliente.id,
        "nome": cliente.nome,
        "descricao": cliente.descricao,
        "cnpj": cliente.cnpj,
        "total_notas": len(cliente.notas),
        "notas": [{"descricao_servico": c.descricao_servico} for c in cliente.notas]
    }


def apresenta_clientes(clientes: List[Cliente]):
    """ Retorna uma representação dos clientes seguindo o schema definido em
        ClienteViewSchema.
    """
    result = []
    for cliente in clientes:
        result.append({
            "id": cliente.id,
            "nome": cliente.nome,
            "descricao": cliente.descricao,
            "cnpj": cliente.cnpj,
        })

    return {"clientes": result}
