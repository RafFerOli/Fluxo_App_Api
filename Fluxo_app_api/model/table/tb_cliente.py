from sqlalchemy import Column, String, Integer, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from  model import Base, Nota


class Cliente(Base):
    __tablename__ = 'cliente'

    id = Column("pk_cliente", Integer, primary_key=True)
    nome = Column(String(90), unique=True)
    descricao = Column(String(400))
    cnpj = Column(String(18), unique=True)
    data_insercao = Column(DateTime, default=datetime.now())

    # Definição do relacionamento entre o cliente e nota fiscal.
    # Essa relação é implicita, não está salva na tabela 'cliente',
    # mas aqui estou deixando para SQLAlchemy a responsabilidade
    # de reconstruir esse relacionamento.
    notas = relationship("Nota")

    def __init__(self, nome:str, descricao:str, cnpj:str,
                 data_insercao:Union[DateTime, None] = None):
        """
        Cadastra um cliente

        Arguments:
            nome: nome do cliente.
            descricao: breve descrição sobre o ramo de ativdades do cliente
            cnpj: cnpj do cliente para uso futuro
            data_insercao: data de quando o cliente foi cadastrado na base
        """       
        self.nome = nome
        self.descricao = descricao
        self.cnpj = cnpj

        # se não for informada, será o data exata da inserção no banco
        if data_insercao:
            self.data_insercao = data_insercao

    def adiciona_nota(self, nota:Nota):
        """ Adiciona um novo comentário ao cliente
        """
        self.notas.append(nota)

