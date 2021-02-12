English/[Português](https://github.com/gabepk/my-devops-notebook/blob/master/README.pt.md)

# My DevOps Notebook

[List of small articles](https://devops-notebook.herokuapp.com) implemented in Django to serve as a repository to my notes on DevOps concepts and tools. I forked the roadmap from [Kamran Ahmedse's repository](https://github.com/kamranahmedse/developer-roadmap) and shaped it according to my current knowledge.

This site was originally created at the [Django Girls](https://djangogirls.org/brasilia/) 2018 event, suported by the [PyLadies DF](http://df.pyladies.com/) organization :heart:

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
