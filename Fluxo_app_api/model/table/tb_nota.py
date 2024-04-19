from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, Float, Boolean
from datetime import datetime
from typing import Union

from  model import Base


class Nota(Base):
    __tablename__ = 'nota'

    id = Column("pk_nota", Integer, primary_key=True)
    numero = Column(Integer, unique=True)
    descricao_servico = Column(String)
    cancelada = Column(Boolean)
    data_emissao = Column(DateTime)
    data_faturamento = Column(DateTime)
    valor = Column(Float)
    data_insercao = Column(DateTime, default=datetime.now())

    # Definição do relacionamento entre o nota e cliente.
    # Aqui está sendo definido a coluna 'cliente' que vai guardar
    # a referencia ao cliente, a chave estrangeira que relaciona
    # um cliente a uma nota fiscal.
    cliente_id = Column(Integer, ForeignKey("cliente.pk_cliente"), nullable=False)

    #def __init__(self, texto:str, data_insercao:Union[DateTime, None] = None):
    def __init__(self, numero:int, descricao_servico:str, cancelada:bool,
                 data_emissao:datetime,data_faturamento:datetime,valor:float,
                 data_insercao:Union[DateTime, None] = None):
        """
        Cadastra uma nota

        Arguments:
            numero: = número da nota fiscal emitida
            descricao_servico: = descrição do serviço realizado
            cancelada: = status da nota fiscal (false = ok / true = cancelada)
            data_emissao: = data_emissao
            data_faturamento: = data_faturamento
            valor: = valor 
            data_insercao: data de quando a nota foi inserida na base
        """

        self.numero = numero
        self.descricao_servico = descricao_servico
        self.cancelada = cancelada
        self.data_emissao = data_emissao
        self.data_faturamento = data_faturamento
        self.valor = valor  
        if data_insercao:
            self.data_insercao = data_insercao
