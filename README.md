## 📦 ERP - Sistema de Gestão Integrada --> Django

Este é um projeto em grupo do qual nós apresentaremos um programa de venda de produtos para mercados.
O objetivo é centralizar e automatizar processos de negócios, abrangendo vendas, estoque, finanças e relacionamento com clientes.

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

## 🛰️ Tecnologias Utilizadas

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)


