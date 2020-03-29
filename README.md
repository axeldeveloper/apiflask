# Web app in python with flask

```
Give examples
```
- python
- postgres
- Microservice
- flask


> CRUD

    CRUD (Create, Read, Update and Delete in English) for the four basic 
    operations used in relational databases (RDBMS) or 
    user interface for creating, querying, updating and destroying data.

## mais informações de instalação do python 3.5

* [aqui](http://www.islandtechph.com/2017/10/23/how-to-deploy-a-flask-python-3-5-application-on-a-live-ubuntu-16-04-linux-server-running-apache2/) - install python


## PIP3
- sudo apt-get install python3-pip  `install`
- upgrade -> pip3 install --upgrade pip `upgrade`



# Python and pipenv 
- pip3 install pipenv
- pipenv shell  `execute to path project`
? Successfully created virtual environment! 
- Virtualenv location: /root/.local/share/virtualenvs/apiflask-qjIn9wD9
- . /root/.local/share/virtualenvs/apiflask-qjIn9wD9/bin/activate



## pipenv set python 
    - pipenv install --python 'c:\python'  <-- `Window`
    - pipenv install --python 'usr/local/bin/python3.x' <-- `linux`
    - pipenv install --python ~/usr/local/bin/python3.7
    - /usr/local/bin/python3.7  pipenv shell 


# Windows - WSL 
- sudo apt update
- sudo apt install python3
- sudo apt install python3-pip
- sudo apt install python3-pip
- pip3 list
- pip3 install pipenv
- pipenv install


# Dependencies 
> $ pip install pipenv
> $ sudo apt install libpq-dev python3-dev
> $ pip3 install psycopg2-binary


# Python initialize pipenv
- pipenv shell


## example output
✔ Successfully created virtual environment! 
- Virtualenv location: /root/.local/share/virtualenvs/apiflask-qjIn9wD9
- . /root/.local/share/virtualenvs/apiflask-qjIn9wD9/bin/activate  `<-  notebocke`
- . /root/.local/share/virtualenvs/apiflask-blOf2lWf/bin/activate  `<-  desktop`
- . /home/axel/.local/share/virtualenvs/apiflask-fC62-enn/bin/activate `<-   WSL Windows desktop`


# Install packages
    * $ pipenv install or
    * $ pipenv install -r requirements.txt


# Flask  migrations
    * $ flask db init
    * $ flask db migrate
    * $ flask db upgrade


# Running the Development Server

First, you need to specify where the Flask application is defined 
(via the FLASK_APP environment variable). 
Then, you can run your Flask application with `flask run`:

- (venv) $ export FLASK_APP=wsgi.py
- (venv) $ export FLASK_ENV=development
- (venv) $ export FLASK_DEBUG=1
- (venv) $ flask run

* Serving Flask app "app"
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
* alternative  

    * $ python -m flask run
    * $ flask run --host=0.0.0.0

# Debug Mode
    * $ export FLASK_ENV=development
    * $ flask run
    * $ export FLASK_DEBUG=1.


# install packages Flask-Migrate
    * $ pip install Flask-Migrate or 
    * $ pipenv install Flask-Migrate

# Migrations 
    * $ flask db init
    * $ flask db migrate 
    * $ flask db migrate -m "Inico do migrate"
    * $ flask db upgrade
    * $ flask db current --verbose
    * $ flask db history
    * $ flask db --help


## Using Flask-Script
>
    db = SQLAlchemy(app)
    migrate = Migrate(app, db)

    manager = Manager(app)
    manager.add_command('db', MigrateCommand)

    class User(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(128))

    if __name__ == '__main__':
        manager.run()


    $ python manage.py db init
    $ python manage.py db migrate
    $ python manage.py db upgrade
    $ python manage.py db --help


# Docker
- sudo usermod -aG docker $USER
- export DOCKER_HOST="tcp://0.0.0.0:2375"
- sudo service docker start or systemctl start docker.
- sudo service docker stop

export DOCKER_HOST=127.0.0.1:4243 >> ~/.bashrc


docker-compose -f "docker/docker-compose.yml" up -d --build

/usr/bin/docker-compose -f "docker/docker-compose.yml" up -d --build

export DOCKER_HOST=tcp://192.168.99.100:2376  // your Docker IP
export DOCKER_CERT_PATH=/mnt/c/Users/YOUR_USERNAME/.docker/machine/certs
export DOCKER_TLS_VERIFY=1
sudo /etc/init.d/docker start
### project using

- [x] python 3.4.4  upgrade pipenv and python 3.5.3
- [x] flask
- [x] psycopg2
- [x] SQLAlchemy
- [x] Flask-SQLAlchemy
- [x] postgresSql
- [x] html
- [x] Jinja

**Disclaimers:**
    * $ git add .
    * $ git commit -am "make it better"
    * $ git push origin master


# Existing Git repository
    * $ git clone url project


# Git config
    * $ git config --global user.email "email@example.com"
    * $ git config --global user.name "ark"