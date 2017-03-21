# E-commerce 

Python 3.5 e Django 1.10

## Descrições do projeto 

Exemplo de um e-commerce, com dois Gateway de pagamento PAGSEGURO & PAYPAL .

## Live Demo

http://lojavirtal.herokuapp.com/

```bash
login : admin
senha : admin1234
```

## Baixando e rodando a app


Siga o passo a passo:

1. Clone o repositório;
2. Crie um virtualenv com Python 3.5;
3. Ative o virtualenv;
4. Instale as dependências;
5. Configure a instância com o .env;
6. Configure o banco de dados de sua preferencia no settings.ini.

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

Dependências:

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
