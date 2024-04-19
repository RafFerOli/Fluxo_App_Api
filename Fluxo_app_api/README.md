# Fluxo App Api

Este pequeno projeto tem como objetivo realizar o controle de notas ficais e despesas para uma pequena empresa de prestação de serviço.

O objetivo aqui é demonstrar parte do conhecimento adquirido durante a disciplina de **Desenvolvimento Full Stack Básico**.

---
## Como executar 


Será necessário ter todas as libs python listadas no `requirements.txt` instaladas.
Após clonar o repositório, é necessário ir ao diretório raiz, pelo terminal, para poder executar os comandos descritos abaixo.

> É fortemente indicado o uso de ambientes virtuais do tipo [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html).

```
(env)$ pip install -r requirements.txt
```

Este comando instala as dependências/bibliotecas, descritas no arquivo `requirements.txt`.

Para executar a API  basta executar:

```
(env)$ flask run --host 0.0.0.0 --port 5000
```

Em modo de desenvolvimento é recomendado executar utilizando o parâmetro reload, que reiniciará o servidor
automaticamente após uma mudança no código fonte. 

```
(env)$ flask run --host 0.0.0.0 --port 5000 --reload
```

Abra o [http://localhost:5000/#/](http://localhost:5000/#/) no navegador para verificar o status da API em execução.

> Para executar o sistema completamente será necessário fazer o download do projeto [Fluxo App Front](https://github.com/RafFerOli/Fluxo_App_Front/tree/main), salvar a pasta Fluxo_app_front e fluxo_app_api no mesmo diretório, abrir o diretório no Visual Studio Code e seguir as instruções de [README.md](https://github.com/RafFerOli/Fluxo_App_Front/blob/main/Fluxo_app_front/README.md).
