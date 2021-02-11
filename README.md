English/[Português](https://github.com/gabepk/my-devops-notebook/blob/master/README.pt.md)

# My DevOps Notebook

[List of small articles](https://devops-notebook.herokuapp.com) implemented in Django to serve as a repository to my notes on DevOps concepts and tools.

<sub>This site was created at the [Django Girls](https://djangogirls.org/brasilia/) 2018 event, suported by the [PyLadies DF](http://df.pyladies.com/) organization :heart:</sub>

## How to Execute

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

Below you find a chart of a roadmap to introduce DevOps to my dev team, demonstrating the paths that we can take and the technologies that we would want to adopt in order to adopt devops.
I forked this chart (a [Balsamiq](https://balsamiq.com/) project) from [Kamran Ahmedse](https://github.com/kamranahmedse/developer-roadmap) and shaped according to my current knowledge (December, 2018).

<img src="./blog/static/img/devops.png?raw=true" align="center" alt="DevOps Roadmap">

[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)
