Português/[English](https://github.com/gabepk/my-devops-notebook/blob/master/README.md)

# Meu Caderno DevOps

[Lista de anotações sobre DevOps](https://devops-notebook.herokuapp.com) implementado no Django para servir como um repositório para minhas anotações sobre conceitos e ferramentas de DevOps.

<sub>Este site foi criado no evento [Django Girls](https://djangogirls.org/brasilia/) 2018, apoiado pelas [PyLadies DF](http://df.pyladies.com/):heart: </sub>

Eu _forkei_ este roadmap do [repositório do Kamran Ahmedse](https://github.com/kamranahmedse/developer-roadmap) e modelei de acordo com meu conhecimento.

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
