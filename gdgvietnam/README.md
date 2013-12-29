## How to develop

Install pip, virtualenv, virtualenvwrapper

[Read tutorial](http://www.jontourage.com/2011/02/09/virtualenv-pip-basics/)

In virtualenv run

```sh
    pip install -r /home/Workspace/gdgvietnam/gdgvietnam/requirements.txt
    pip install -e pip install -e /home/Workspace/gdgvietnam/mezzanine-events/
```

Clone source code

```sh
    git clone -b develop https://github.com/gdgvietnam/gdgvietnam.git
    /home/username/.virtualenvs/gdgvietnam/bin/python /home/Workspace/gdgvietnam/gdgvietnam/manage.py runserver 8000
```

Account demo

- Username: nampnq
- Pass: 1