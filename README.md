# Target Map Project - JOIN Company

## Descrição

O **Target Map** é um projeto baseado em Django que permite visualizar alvos (targets) em um mapa interativo utilizando a API do Google Maps. Além disso, o sistema oferece funcionalidades para criar novos alvos com coordenadas geográficas e data de expiração. A aplicação foi construída para demonstrar como integrar dados geoespaciais com um backend Django e uma interface frontend utilizando JavaScript.

## Funcionalidades

- **Exibir Alvos no Mapa**: O mapa é exibido com marcadores representando os alvos cadastrados.
- **Criar Novos Alvos**: Através de um formulário, o usuário pode adicionar novos alvos com nome, latitude, longitude e data de expiração.
- **Exibição Dinâmica**: Ao salvar um novo alvo, a página é atualizada automaticamente para mostrar a nova localização no mapa.

## Tecnologias Utilizadas

- **Django**: Framework de backend para desenvolvimento web.
- **PostgreSQL**: Banco de dados relacional utilizado para armazenar os dados dos alvos.
- **Google Maps API**: Para renderizar o mapa e exibir os marcadores dos alvos.
- **JavaScript** (com jQuery): Para interações no frontend, como exibição do mapa e manipulação do formulário.
- **Django REST Framework**: Para criar uma API RESTful que manipula as operações de CRUD para os alvos.
- **HTML/CSS**: Estrutura e estilo da página.

## Instalação

### Pré-requisitos

- Python 3.x
- Django 5.x
- PostgreSQL (ou outro banco de dados compatível)

### Passos para Rodar o Projeto Localmente

1. **Clone o repositório:**
