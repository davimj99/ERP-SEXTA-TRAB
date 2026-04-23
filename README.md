## 📦 ERP - Sistema de Gestão Integrada --> Django

Este é um projeto em grupo do qual nós apresentaremos um programa de venda de produtos para mercados.
O objetivo é centralizar e automatizar processos de negócios, abrangendo vendas, estoque, finanças e relacionamento com clientes.

## 📌 Sobre o Projeto
O ERP-SEXTA-TRAB é um sistema de Enterprise Resource Planning (Planejamento de Recursos Empresariais) desenvolvido como um projeto acadêmico/técnico. O objetivo principal é centralizar a gestão de processos operacionais, permitindo que diferentes setores de uma empresa (como Vendas, Cadastro e Administrativo) compartilhem informações de forma integrada e segura.

Este sistema foi construído utilizando o framework Django, aproveitando sua arquitetura robusta de Model-View-Template (MVT) para garantir um desenvolvimento ágil e seguro.

## 🚀 Visão Arquitetural e Tecnologias

O projeto foi desenvolvido sob os princípios da programação orientada a objetos (POO) e estruturado no padrão **MVT (Model-View-Template)**. A modularidade foi priorizada para garantir um código limpo, coeso e de fácil escalabilidade.

* **Linguagem:** Python 3.x
* **Framework:** Django
* **Banco de Dados:** SQLite (padrão de desenvolvimento)
* **Interface Web:** HTML5, CSS3, Django Templates

## 🧩 Estrutura de Módulos (Apps)

A regra de negócio do ERP está distribuída de forma isolada nas seguintes aplicações:

* `erp/`: Core do projeto, contendo configurações globais, roteamento raiz e definições ASGI/WSGI.
* `usuarios/`: Gestão de autenticação, controle de sessões e permissões de acesso.
* `clientes/`: Cadastro e manutenção da base de clientes (PF e PJ).
* `produtos/`: Gerenciamento do catálogo de itens comercializados.
* `estoque/`: Controle de inventário, registro de entradas e saídas de mercadorias.
* `vendas/`: Orquestração do processo de vendas, integrando entidades de clientes, produtos e gerando impacto no estoque.
* `financeiro/`: Gestão do fluxo de caixa, contas a pagar e a receber.

## 🧩 Arquitetura Modular (Divisão do ERP)

* **Core / Base:**

➦Gerenciamento de usuários e permissões (Controle de Acesso).

➦Configurações globais do sistema.

➦Templates base (menus laterais, cabeçalhos).

* **Gerenciamento de usuários e permissões (Controle de Acesso).**

➦Clientes (Pessoa Física / Pessoa Jurídica).

➦Fornecedores.

* **Módulo de Materiais/Estoque:**

➦Cadastro de Produtos e Categorias.

➦Controle de entrada e saída (Movimentações).

* **Módulo de Vendas (Operacional):**

➦Orçamentos e Pedidos.

➦Integração direta com o Estoque (baixar itens vendidos) e com o Financeiro (gerar contas a receber).

## 🛰️ Tecnologias Utilizadas

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white) 🔁
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)

## ✨ Principais Funcionalidades

- **👥 Gestão de Cadastros (CRUD):** Administração completa de clientes, fornecedores e colaboradores.
- **🔐 Controle de Acesso e Segurança:** Sistema de autenticação nativo do Django, com divisão de permissões por grupos de usuários (Administradores, Gerentes, Operadores).
- **📊 Painel Administrativo (Admin Panel):** Interface customizada para gerenciamento rápido de registros do banco de dados.
- **🔄 Automação de Fluxos:** Interligação de módulos (ex: uma venda atualiza automaticamente o estoque).
- **📈 Relatórios Básicos:** Geração de visualizações para tomada de decisão (em implementação).
- **🚧Arquitetura Escalável:** Organização modular para facilitar a inclusão de novos departamentos (RH, Financeiro, Estoque).

## 🔄 Fluxo de Informação
```text
[ Cliente (Navegador) ] 
       │ 
       ▼ (1. Requisição HTTP - Ex: /vendas/nova)
[ Roteador (urls.py) ] 
       │ 
       ▼ (2. Encaminha para a View correta)
[ View (views.py) ] ◀━━━━┓ (4. Retorna os dados do banco)
       │                 ┃
       ▼ (3. Consulta)   ┃
[ Model (models.py) ] ━━━┛
       │ 
       ▼ (5. Acessa o Banco de Dados)
[ Banco de Dados (SQLite/PostgreSQL) ]

(6. View compila os dados com o HTML)
[ View ] ━━━▶ [ Template (HTML/CSS) ]
                     │
                     ▼ (7. Resposta HTTP - Renderiza a tela)
             [ Cliente (Navegador) ]
```
## 📂 Estrutura do Repositório

```text
📦 ERP-SEXTA-TRAB
 ┣ 📂 core/                # Configurações globais do projeto (settings.py, urls.py)
 ┣ 📂 apps/                # Módulos independentes do ERP
 ┃ ┣ 📂 clientes/          # Lógica de gestão de clientes
 ┃ ┣ 📂 vendas/            # Fluxo de vendas e pedidos
 ┃ ┗ 📂 estoque/           # Controle de inventário
 ┣ 📂 templates/           # Arquivos HTML base e fragmentos visuais
 ┣ 📂 static/              # Arquivos estáticos (CSS, JS, Imagens)
 ┣ 📜 requirements.txt     # Dependências do projeto
 ┣ 📜 manage.py            # CLI do Django
 ┗ 📜 README.md            # Documentação principal
```


