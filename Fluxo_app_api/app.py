from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from urllib.parse import unquote

from sqlalchemy.exc import IntegrityError
from sqlalchemy import func
from datetime import datetime

from model import Session, Cliente, Nota, Despesa
from logger import logger
from schemas import *
from flask_cors import CORS

info = Info(title="API - Fluxo de Caixa", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# definindo tags

home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
cliente_tag = Tag(name="Cliente", description="Adição, visualização e remoção de clientes na base")
nota_tag = Tag(name="Nota", description="Adição, visualização e remoção de notas fiscais na base")
despesa_tag = Tag(name="Despesa", description="Adição, visualização e remoção de despesas na base")

# Rota da Documentação


@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')

#-------------------------------------------------------------------------------------
# Requisições do Cliente
#-------------------------------------------------------------------------------------

@app.post('/Cliente', tags=[cliente_tag],
          responses={"200": ClienteViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def add_Cliente(form: ClienteSchema):
    """Adiciona um novo cliente à base de dados

    Retorna uma representação dos clientes e notas fiscais associadas.
    """
    cliente = Cliente(
        nome=form.nome,
        descricao=form.descricao,
        cnpj=form.cnpj)
    logger.debug(f"Adicionando cliente de nome: '{cliente.nome}'")
    try:
        # criando conexão com a base
        session = Session()
        # adicionando Cliente
        session.add(cliente)
        # efetivando o camando de adição de novo item na tabela
        session.commit()
        logger.debug(f"Adicionado cliente de nome: '{cliente.nome}'")
        return apresenta_cliente(cliente), 200

    except IntegrityError as e:
        # como a duplicidade do nome é a provável razão do IntegrityError
        error_msg = "Cliente de mesmo nome ou cnpj já salvo na base :/"
        logger.warning(f"Erro ao adicionar cliente '{cliente.nome}', {error_msg}")
        return {"mesage": error_msg}, 409

    except Exception as e:
        # caso um erro fora do previsto
        error_msg = "Não foi possível salvar novo item :/"
        logger.warning(f"Erro ao adicionar cliente '{cliente.nome}', {error_msg}")
        return {"mesage": error_msg}, 400


@app.delete('/Cliente', tags=[cliente_tag],
            responses={"200": ClienteDelSchema, "404": ErrorSchema})
def del_Cliente(query: ClienteBuscaSchema):
    """Deleta um cliente a partir do nome de cliente informado

    Retorna uma mensagem de confirmação da remoção.
    """
    cliente_nome = unquote(unquote(query.nome))
    print(cliente_nome)
    logger.debug(f"Deletando dados sobre o cliente #{cliente_nome}")
    # criando conexão com a base
    session = Session()
    # fazendo a remoção
    count = session.query(Cliente).filter(Cliente.nome == cliente_nome).delete()
    session.commit()

    if count:
        # retorna a representação da mensagem de confirmação
        logger.debug(f"Deletado Cliente #{cliente_nome}")
        return {"mesage": "Cliente removido", "id": cliente_nome}
    else:
        # se o Cliente não foi encontrado
        error_msg = "Cliente não encontrado na base :/"
        logger.warning(f"Erro ao deletar Cliente #'{cliente_nome}', {error_msg}")
        return {"mesage": error_msg}, 404


@app.get('/Clientes', tags=[cliente_tag],
         responses={"200": ListagemClientesSchema, "404": ErrorSchema})
def get_Clientes():
    """Faz a busca por todos os clientes cadastrados

    Retorna uma representação da listagem de clientes.
    """
    logger.debug(f"Coletando clientes ")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    clientes = session.query(Cliente).all()

    if not clientes:
        # se não há Clientes cadastrados
        return {"Clientes": []}, 200
    else:
        logger.debug(f"%d rodutos econtrados" % len(clientes))
        # retorna a representação de Cliente
        print(clientes)
        return apresenta_clientes(clientes), 200


@app.get('/Cliente', tags=[cliente_tag],
         responses={"200": ClienteViewSchema, "404": ErrorSchema})
def get_Cliente(query: ClienteBuscaSchema):
    """Faz a busca por um cliente a partir do nome do cliente

    Retorna uma representação do cliente e das notas associadas.
    """
    cliente_nome = query.nome
    logger.debug(f"Coletando dados sobre o cliente #{cliente_nome}")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    cliente = session.query(Cliente).filter(func.lower(Cliente.nome) == cliente_nome.lower()).first()

    if not cliente:
        # se o cliente não foi encontrado
        error_msg = "Cliente não encontrado na base :/"
        logger.warning(f"Erro ao buscar cliente '{cliente_nome}', {error_msg}")
        return {"mesage": error_msg}, 404
    else:
        logger.debug(f"Cliente econtrado: '{cliente.nome}'")
        # retorna a representação de Cliente
        return apresenta_cliente(cliente), 200
   
#-------------------------------------------------------------------------------------
# Requisições da Despesa
#-------------------------------------------------------------------------------------

@app.post('/Despesa', tags=[despesa_tag],
          responses={"200": DespesaSchema, "409": ErrorSchema, "400": ErrorSchema})
def add_Despesa(form: DespesaSchema):
    """Adiciona uma nova despesa à base de dadas

    Retorna uma representação das despesas associadas.
    """
    despesa = Despesa(
        descricao = form.descricao,
        data = datetime.strptime(form.data,"%d/%m/%Y"),
        valor = form.valor)
    logger.debug(f"Adicionanda despesa de descrição: '{despesa.descricao}'")
    try:
        # criando conexão com a base
        session = Session()
        # adicionando Despesa
        session.add(despesa)
        # efetivando o comando de adição de novo item na tabela
        session.commit()
        logger.debug(f"Adicionada despesa de descrição: '{despesa.descricao}'")
        return apresenta_despesa(despesa), 200

    except Exception as e:
        # caso um erro fora da previsto
        error_msg = "Não foi possível salvar novo item :/"
        logger.warning(f"Erro ao adicionar despesa '{despesa.nome}', {error_msg}")
        return {"mesage": error_msg}, 400


@app.delete('/Despesa', tags=[despesa_tag],
            responses={"200": DespesaDelSchema, "404": ErrorSchema})
def del_Despesa(query: DespesaBuscaIdSchema):
    """Deleta uma despesa a partir do id de despesa informado

    Retorna uma mensagem de confirmação da remoção.
    """
    despesa_id = query.id
    print(despesa_id)
    logger.debug(f"Deletando dados sobre a despesa #{despesa_id}")
    # criando conexão com a base
    session = Session()
    # fazendo a remoção
    count = session.query(Despesa).filter(Despesa.id == despesa_id).delete()
    session.commit()

    if count:
        # retorna a representação da mensagem de confirmação
        logger.debug(f"Deletada Despesa #{despesa_id}")
        return {"mesage": "Despesa removida", "id": despesa_id}
    else:
        # se a despesa não foi encontrado
        error_msg = "Despesa não encontrada na base :/"
        logger.warning(f"Erro ao deletar Despesa #'{despesa_id}', {error_msg}")
        return {"mesage": error_msg}, 404


@app.get('/Despesas', tags=[despesa_tag],
         responses={"200": ListagemDespesasSchema, "404": ErrorSchema})
def get_Despesas():
    """Faz a busca por todas as despesas cadastradas

    Retorna uma representação da listagem de despesas.
    """
    logger.debug(f"Coletanda despesas ")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    despesas = session.query(Despesa).all()

    if not despesas:
        # se não há despesas cadastradas
        return {"Despesas": []}, 200
    else:
        logger.debug(f"%d rodutos econtradas" % len(despesas))
        # retorna a representação de despesa
        print(despesas)
        return apresenta_despesas(despesas), 200


@app.get('/Despesa', tags=[despesa_tag],
         responses={"200": ListagemDespesasSchema, "404": ErrorSchema})
def get_Despesa(query: DespesaBuscaDataSchema):
    """Faz a busca por um grupo de despesas a partir do intervalo fornecido

    Retorna uma representação das despesas no intervalo desejado.
    """
    #pegando datas para pesquisa
    despesa_data_ini = datetime.strptime(query.data_ini,"%d/%m/%Y")
    despesa_data_fin = datetime.strptime(query.data_fin,"%d/%m/%Y")
    logger.debug(f"Coletando dados sobre as despesas")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    despesas = session.query(Despesa).filter((Despesa.data >= despesa_data_ini)&(Despesa.data <= despesa_data_fin))

    if not despesas:
        # se as despesas não forem encontradas
        error_msg = "Despesas não encontradas na base :/"
        logger.warning(f"Erro ao buscar as despesas entre: '{query.data_ini}' e '{query.data_fin}', {error_msg}")
        return {"mesage": error_msg}, 404
    else:
        logger.debug(f"Despesas encontradas entre: '{query.data_ini}' e '{query.data_fin}'")
        # retorna a representação de despesa
        return apresenta_despesas(despesas), 200

#-------------------------------------------------------------------------------------
# Requisições da Nota
#-------------------------------------------------------------------------------------

@app.post('/Nota', tags=[nota_tag],
          responses={"200": NotaSchema, "409": ErrorSchema, "400": ErrorSchema})
def add_Nota(form: NotaSchema):
    """Adiciona uma nova nota à base de dadas

    Retorna uma representação das notas associadas.
    """
    try:
        cliente_id = form.cliente_id

        logger.debug(f"Adicionando nota ao cliente #{cliente_id}")
        # criando conexão com a base
        session = Session()
        # fazendo a busca pelo cliente
        cliente = session.query(Cliente).filter(Cliente.id == cliente_id).first()

        if not cliente:
            # se cliente não for encontrado
            error_msg = "Cliente não encontrado na base :/"
            logger.warning(f"Erro ao adicionar nota ao cliente '{str(cliente_id)}', {str(error_msg)}")
            return {"mesage": error_msg}, 404
    
        # criando a nota
        nota = Nota(
                numero = form.numero,
                descricao_servico = form.descricao_servico,
                cancelada = form.cancelada,
                data_emissao =  datetime.strptime(form.data_emissao,"%d/%m/%Y"),
                data_faturamento =  datetime.strptime(form.data_faturamento,"%d/%m/%Y"),
                valor = form.valor)
    
        # adicionando o comentário ao produto
        cliente.adiciona_nota(nota)
        session.commit()

        logger.debug(f"Adicionado nota ao cliente #{cliente_id}")

        # retorna a representação de produto
        return apresenta_nota(nota), 200

    except Exception as e:
        # caso um erro fora da previsto
        error_msg = "Não foi possível salvar novo item :/"
        logger.warning(f"Erro ao adicionar nota '{str(cliente_id)}', {str(error_msg)}")
        return {"mesage": error_msg}, 400

@app.delete('/Nota', tags=[nota_tag],
            responses={"200": NotaDelSchema, "404": ErrorSchema})
def del_Nota(query: NotaBuscaIdSchema):
    """Deleta uma nota a partir do numero de nota informado

    Retorna uma mensagem de confirmação da remoção.
    """
    nota_numero = query.numero
    print(nota_numero)
    logger.debug(f"Deletando dados sobre a nota #{nota_numero}")
    # criando conexão com a base
    session = Session()
    # fazendo a remoção
    count = session.query(Nota).filter(Nota.numero == nota_numero).delete()
    session.commit()

    if count:
        # retorna a representação da mensagem de confirmação
        logger.debug(f"Deletada Nota #{nota_numero}")
        return {"mesage": "Nota removida", "numero": nota_numero}
    else:
        # se o Nota não foi encontrado
        error_msg = "Nota não encontrada na base :/"
        logger.warning(f"Erro ao deletar Nota #'{nota_numero}', {error_msg}")
        return {"mesage": error_msg}, 404


@app.get('/Notas', tags=[nota_tag],
         responses={"200": ListagemNotasSchema, "404": ErrorSchema})
def get_Notas():
    """Faz a busca por todas as notas cadastradas

    Retorna uma representação da listagem de notas.
    """
    logger.debug(f"Coletando notas ")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    notas = session.query(Nota).all()

    if not notas:
        # se não há notas cadastradas
        return {"Notas": []}, 200
    else:
        logger.debug(f"%d rodutos econtradas" % len(notas))
        # retorna a representação de nota
        print(notas)
        return apresenta_notas(notas), 200


@app.get('/Nota', tags=[nota_tag],
         responses={"200": ListagemNotasSchema, "404": ErrorSchema})
def get_Nota(query: NotaBuscaDataSchema):
    """Faz a busca por um grupo de notas a partir do intervalo de emissão fornecido

    Retorna uma representação das notas no intervalo desejado.
    """
    #pegando datas para pesquisa
    nota_data_ini = datetime.strptime(query.data_ini,"%d/%m/%Y")
    nota_data_fin = datetime.strptime(query.data_fin,"%d/%m/%Y")
    logger.debug(f"Coletando dados sobre as notas")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    notas = session.query(Nota).filter((Nota.data_emissao >= nota_data_ini)&(Nota.data_emissao <= nota_data_fin))

    if not notas:
        # se as notas não forem encontradas
        error_msg = "Notas não encontradas na base :/"
        logger.warning(f"Erro ao buscar as notas entre: '{query.data_ini}' e '{query.data_fin}', {error_msg}")
        return {"mesage": error_msg}, 404
    else:
        logger.debug(f"Notas encontradas entre: '{query.data_ini}' e '{query.data_fin}'")
        # retorna a representação de Nota
        return apresenta_notas(notas), 200

