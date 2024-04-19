from pydantic import BaseModel
from typing import Optional, List
from model.table.tb_despesa import Despesa
from datetime import datetime

class DespesaSchema(BaseModel):
    """ Define como uma nova despesa a ser inserida deve ser representada
    """
    descricao: str = "Conta de luz"
    data: str = "17/04/2024"
    valor: float = 100.0


class DespesaViewSchema(BaseModel):
    """ Define como um conjunto de despesas será retornado
    """
    id: int = 1
    descricao: str = "Conta de luz"
    data: str = "17/04/2024"
    valor: float = 100.0


class DespesaBuscaIdSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no id da despesa.
    """
    id: int = 1


class DespesaBuscaDataSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base em um intervalo da despesa.
    """
    data_ini: str = "01/01/2024"
    data_fin: str = "31/12/2024"


class ListagemDespesasSchema(BaseModel):
    """ Define como uma listagem de despesas será retornada.
    """
    despesas:List[DespesaViewSchema]  


class DespesaDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    mesage: str
    descricao: str


def apresenta_despesa(despesa: Despesa):
    """ Retorna uma representação da despesa seguindo o schema definido em
        DespesaSchema.
    """
    return {
        "descricao": despesa.descricao,
        "data": despesa.data,
        "valor": despesa.valor
    }


def apresenta_despesas(despesas: List[Despesa]):
    """ Retorna uma representação das despesas seguindo o schema definido em
        DespesaSchema.
    """
    result = []
    for despesa in despesas:
        result.append({
        "id":despesa.id,
        "descricao": despesa.descricao,
        "data": despesa.data,
        "valor": despesa.valor,
        })

    return {"despesas": result}
