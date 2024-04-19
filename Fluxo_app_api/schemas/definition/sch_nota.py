from pydantic import BaseModel
from typing import Optional, List
from model.table.tb_nota import Nota
from datetime import datetime

class NotaSchema(BaseModel):
    """ Define como uma nova nota a ser inserida deve ser representada
    """   
    cliente_id: int = 1
    numero: int = 1
    descricao_servico: str = "sol e praia"
    cancelada: bool = False
    data_emissao: str = "18/04/2024"
    data_faturamento: str = "18/04/2024"
    valor: float = 10000.0


class NotaViewSchema(BaseModel):
    """ Define como um conjunto de notas será retornado
    """
    id: int = 1
    cliente_id: int = 1
    numero: int = 1
    descricao_servico: str = "sol e praia"
    cancelada: bool = False
    data_emissao: str = "18/04/2024"
    data_faturamento: str = "18/04/2024"
    valor: float = 10000.0


class NotaBuscaIdSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no numero de emissão da nota.
    """
    numero: int = 1


class NotaBuscaDataSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base em um intervalo de emissão da nota.
    """
    data_ini: str = "01/01/2024"
    data_fin: str = "31/12/2024"


class ListagemNotasSchema(BaseModel):
    """ Define como uma listagem de notas será retornada.
    """
    notas:List[NotaViewSchema]  


class NotaDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    mesage: str
    descricao: str


def apresenta_nota(nota: Nota):
    """ Retorna uma representação da nota seguindo o schema definido em
        NotaSchema.
    """
    return {
        "cliente_id": nota.cliente_id ,
        "numero": nota.numero ,
        "descricao_servico": nota.descricao_servico ,
        "cancelada": nota.cancelada ,
        "data_emissao": nota.data_emissao ,
        "data_faturamento": nota.data_faturamento ,
        "valor": nota.valor
    }


def apresenta_notas(notas: List[Nota]):
    """ Retorna uma representação das notas seguindo o schema definido em
        NotaSchema.
    """
    result = []
    for nota in notas:
        result.append({
        "id": nota.id ,
        "cliente_id": nota.cliente_id ,
        "numero": nota.numero ,
        "descricao_servico": nota.descricao_servico ,
        "cancelada": nota.cancelada ,
        "data_emissao": nota.data_emissao ,
        "data_faturamento": nota.data_faturamento ,
        "valor": nota.valor
        })

    return {"notas": result}
