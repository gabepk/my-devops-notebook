Português/[English](https://github.com/gabepk/my-devops-notebook/blob/master/README.md)

# Meu Caderno DevOps

[Lista de anotações sobre DevOps](https://devops-notebook.herokuapp.com) implementado no Django para servir como um repositório para minhas anotações sobre conceitos e ferramentas de DevOps. Eu _forkei_ este roadmap do [repositório do Kamran Ahmedse](https://github.com/kamranahmedse/developer-roadmap) e modelei de acordo com meu conhecimento.

Este site foi criado originalmente no evento [Django Girls](https://djangogirls.org/brasilia/) 2018, apoiado pelas [PyLadies DF](http://df.pyladies.com/):heart:

# Tópicos adicionais

Eu adicionei alguns tópicos extras relacionados a Amazon (minha empresa atualmente).

- IAM - AWS Identity and Access Management
- ECS - Amazon Elastic Container Service
- CodePipeline - CI/DI tool

## Como executar

### Linux

```console
$ python3 -m venv venv
$ source venv/bin/activate
(venv) $ env LDFLAGS="-I/usr/local/opt/openssl/include -L/usr/local/opt/openssl/lib" pip --no-cache install psycopg2
(venv) $ pip install -r requirements.txt
(venv) $ python manage.py runserver
```

### Windows

```console
$ virtualenv venv
$ venv\Scripts\activate
(venv) $ pip install -r requirements.txt
(venv) $ python manage.py runserver
```
