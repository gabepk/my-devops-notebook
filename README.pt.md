Português/[English](https://github.com/gabepk/my-devops-notebook/blob/master/README.md)

# Meu Caderno DevOps

[Lista de anotações sobre DevOps](https://devops-notebook.herokuapp.com) implementado no Django para servir como um repositório para minhas anotações sobre conceitos e ferramentas de DevOps.

<sub>Este site foi criado no evento [Django Girls](https://djangogirls.org/brasilia/) 2018, apoiado pelas [PyLadies DF](http://df.pyladies.com/):heart: </sub>

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

## DevOps Roadmap 2019

O gráfico abaixo é um roteiro para apresentar o DevOps à minha equipe de desenvolvimento, demonstrando os caminhos que podemos seguir e as tecnologias que podemos de aprender para adotar devops.
Eu _forkei_ este gráfico (um projeto [Balsamiq](https://balsamiq.com/)) de [Kamran Ahmedse](https://github.com/kamranahmedse/developer-roadmap) e modelei de acordo com meu conhecimento de Dezembro de 2018.

<img src="./blog/static/img/devops.png?raw=true" align="center" alt="DevOps Roadmap">

[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)
