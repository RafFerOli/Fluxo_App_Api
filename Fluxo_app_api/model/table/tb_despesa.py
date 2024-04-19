from sqlalchemy import Column, String, Integer, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from  model import Base


class Despesa(Base):
    __tablename__ = 'despesa'

    id = Column("pk_despesa", Integer, primary_key=True)
    descricao = Column(String(250))
    data = Column(DateTime)
    valor = Column(Float)  
    data_insercao = Column(DateTime, default=datetime.now())

    def __init__(self, descricao:str, data:datetime, valor:float,
                 data_insercao:Union[DateTime, None] = None):
        """
        Cadastra uma despesa

        Arguments:            
            descricao: = descrição da despesa realizada
            data: = data de realização da despesa
            valor: = valor da despesa
            data_insercao = data de quando a despesa foi cadastrada
        """
        self.descricao = descricao
        self.data = data
        self.valor = valor  

        # se não for informada, será o data exata da inserção no banco
        if data_insercao:
            self.data_insercao = data_insercao

