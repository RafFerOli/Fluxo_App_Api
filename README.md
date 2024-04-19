# Projeto de API Web em Python para Gestão de Fluxo de Caixa

A gestão eficiente do fluxo de caixa é crucial para o sucesso de qualquer empresa, especialmente para pequenas empresas. Para facilitar esse processo, foi desenvolvida uma API Web em Python que oferece uma solução abrangente e intuitiva para gerenciar o fluxo de caixa.

## Estrutura da API:

A API é construída em Python, utilizando o framework Flask para criar endpoints robustos e escaláveis. Ela é composta por três principais tabelas:

   **Cliente:** Armazena informações sobre os clientes da empresa, como nome, descrição do ramo de atividades e outras informações relevantes.

   **Nota:** Contém detalhes sobre as transações de vendas, incluindo o valor, data e cliente associado através de um relacionamento.

   **Despesa:** Registra os gastos da empresa, incluindo informações como data, descrição e valor.

## Funcionalidades Principais:

   **Gestão de Notas Fiscais:**
        Endpoint para listar, criar e excluir notas fiscais.
        Relacionamento com a tabela de clientes para associar cada nota a um cliente específico.

   **Gestão de Clientes:**
        Funcionalidades para listar, adicionar e excluir informações de clientes.

  **Gestão de Despesas:**
        Endpoint para gerenciar despesas, permitindo a adição e remoção de registros de despesas.

  **Cálculo do Fluxo de Caixa:**
        (Apenas no front-end) Uma página dedicada para calcular a diferença entre o total de notas fiscais não canceladas e despesas, fornecendo uma visão clara do fluxo de caixa atual da empresa.

## Tecnologias Utilizadas:

   **Python:** Linguagem de programação principal para o desenvolvimento da API.
   **Flask:** Framework web leve e flexível para criar endpoints RESTful.
   **SQLAlchemy:** Biblioteca para interagir com o banco de dados SQL de forma simplificada.
   **SQLite:** Banco de dados embutido para armazenamento de dados de forma eficiente e confiável.

## Benefícios:

   **Automatização:** Reduz a necessidade de tarefas manuais na gestão do fluxo de caixa, economizando tempo e recursos.
   **Transparência:** Oferece uma visão clara e transparente das finanças da empresa, facilitando a tomada de decisões.
   **Facilidade de Uso:** Interface intuitiva e amigável para facilitar o uso por parte dos usuários, mesmo aqueles com pouca experiência técnica.

Com essa API, deseja-se fornecer às pequenas empresas uma ferramenta poderosa para gerenciar seu fluxo de caixa de forma eficiente, ajudando no crescimento e sucesso contínuo de seus negócios.
