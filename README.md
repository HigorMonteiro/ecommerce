# Registro de Produtos

Python 3.5 e Django 1.10

## Objetivo

Sistema para controle de proditos com controle de acesso .

Cadastro do codigo e nome do produto.

## Live Demo

http://appecommerce.herokuapp.com/

```bash
login : admin
senha : admin1234
```

## Baixando e rodando a app


siga o passo a passo.

1. Clone o repositório.
2. Crie um virtualenv com Python 3.5
3. Ative o virtualenv.
4. Instale as dependências.
5. Configure a instância com o .env
6. Configure o banco de dados de sua preferencia no settings.ini

```bash
$ git clone https://github.com/HigorMonteiro/ecommerce
$ cd ecommerce
$ virtualenv .env -p /usr/bin/python3.5
$ source .venv/bin/activate
$ pip install -r requirements.txt
$ python manage.py migrate
$ python manage.py runserver
```

#### Usando Docker

Dependêcias

- [docker](https://www.docker.com/)
- [docker-compose](https://docs.docker.com/compose/)

```sh
$ git clone https://github.com/HigorMonteiro/ecommerce
$ cd ecommerce
$ docker-compose build
$ docker-compose run web python manage.py migrate
$ docker-compose run web python manage.py createsuperuser
$ docker-compose up
```
