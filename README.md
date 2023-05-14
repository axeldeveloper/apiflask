# Web app in python with flask
    
    - python
    - postgres
    - Microservice
    - flask 


# CRUD

    CRUD (Create, Read, Update and Delete in English) for the four basic 

# Crete virtual env
    $ python3.9 -m venv env
    $ source env/bin/activate
    (env)$ pip install flask==1.1.2

# PIP3

sudo apt-get install python3-pip  `install`

upgrade -> pip3 install --upgrade pip `upgrade`


# Python and pipenv

pip3 install pipenv

pipenv shell  `execute to path project`


# pipenv set python 
pipenv install --python 'c:\python'  <-- `Window`

pipenv install --python 'usr/local/bin/python3.x' <-- `linux`

pipenv install --python ~/usr/local/bin/python3.7
/usr/local/bin/python3.7  pipenv shell 


# Windows - WSL 
    - sudo apt update
    - sudo apt install python3
    - sudo apt install python3-pip
    - sudo apt install python3-pip
    - pip3 list
    - pip3 install pipenv
    - pipenv install



# Dependencies 
    $ pip install pipenv
    $ sudo apt install libpq-dev python3-dev
    $ pip3 install psycopg2-binary


# Python initialize pipenv
    - pipenv shell


## example output
✔ Successfully created virtual environment! 
- Virtualenv location: /root/.local/share/virtualenvs/apiflask-qjIn9wD9
- . /root/.local/share/virtualenvs/apiflask-qjIn9wD9/bin/activate  `<-  env`


# Install packages
    $ pipenv install or
    $ pipenv install -r requirements.txt


# Running the Development Server

Flask application with `flask run`:

    - (venv) $ export FLASK_ENV=development
    - (venv) $ export FLASK_DEBUG=1
    - (venv) $ export FLASK_APP=app.py
    - (venv) $ flask run

## output 

    * Serving Flask app "app"
    * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
    * alternative  

        * $ python -m flask run
        * $ flask run --host=0.0.0.0

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

# Flask  migrations
    * $ flask db init
    * $ flask db migrate
    * $ flask db upgrade
    docker-compose run -rm api flask db migrate



## Using Flask-Script
```python
    
    db = SQLAlchemy(app)
    migrate = Migrate(app, db)

    manager = Manager(app)
    manager.add_command('db', MigrateCommand)

    class User(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(128))

    if __name__ == '__main__':
        manager.run()

```

# query functions
```python
    # (1) all() 
    data = User.query.all()
    print(data)


    #(2) filter() 
    >
    <
    >=
    <=
    ==
    !=
    data = User.query.filter(User.sex==True,User.age<20) 
    data = User.query.filter()


    # (3) filter_by() 
    data = User.query.filter_by()
    data = User.query.filter_by(sex=True)
    data = User.query.filter_by(sex=True,age=18)

    # (4) offset(num) 
    data = User.query.offset(5)

    # (5) limit(num) 
    data = User.query.limit(5)

    # (6) offset limit
    data = User.query.offset(5).limit(5)

    # (7) order_by
    data = User.query.order_by(User.age)
    data = User.query.order_by(-User.age)


    # (8) first() 
    data = User.query.order_by(-User.age).first()
    data = User.query.first()


    # (9) get(id)
    data = User.query.get(1)

    # (10) contains() 
    data = User.query.filter(User.username.contains('张'))

    # (11) like
    data = User.query.filter(User.username.like('%hello%'))
    data = User.query.filter(User.username.like('hello%'))
    data = User.query.filter(User.username.like('%hello'))


    # (12) startswith endswith 
    data = User.query.filter(User.username.startswith('hello'))
    data = User.query.filter(User.username.endswith('world'))


    # (13) 
    __gt__
    __ge__
    __lt__
    __le__
    data = User.query.filter(User.age.__gt__(30))

    # (14) in and not … in …
    data = User.query.filter(User.age.in_([10,20,30,40,18,91]))
    data = User.query.filter(User.age.notin_([10,20,30,40,18,91]))


    # (15) null and not null
    data = User.query.filter(User.username.is_(None))
    data = User.query.filter(User.username==None)
    data = User.query.filter(User.username!=None)
    data = User.query.filter(User.username.isnot(None))


    # (16) and_
    from sqlalchemy import and_
    data = User.query.filter(and_(User.sex==True,User.age==18))
    data = User.query.filter(User.sex==True,User.age==18)
    data = User.query.filter(User.sex==True).filter(User.age==18)


    # (17) or_
    from sqlalchemy import or_
    data = User.query.filter(or_(User.sex==True,User.age==18))


    # (18) not_
    from sqlalchemy import not_
    data = User.query.filter(not_(User.sex == True))

    # (19) count 
    data = User.query.filter().count()

    # (20) concat 
    data = User.query.order_by(-Posts.path.concat(Posts.id))
```


# manage congigure and use
- $ python manage.py db init
- $ python manage.py db migrate
- $ python manage.py db upgrade
- $ python manage.py db --help
- docker exec -i flask_api flask db ini
- docker exec -i flask_api flask db migrate -m "Initial migration." 
- docker exec -i flask_api flask db upgrade   



# doccker compose
- docker-compose -f "docker/docker-compose.yml" up -d --build



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
    * $git rm -r --cached . `resolve problem cache`


# Existing Git repository
    * $ git clone url project


# Git config
    * $ git config --global user.email "email@example.com"
    * $ git config --global user.name "ark"


```python

@api.route('/create_table/')
def create_table():
    db.create_all()
    return 'create_table'
    
@api.route('/drop_table/')
def drop_table():
    db.drop_all()
    return 'drop_table'


@manager.command
def createdb():
    db.create_all()
    return 'create_table'

@manager.command
def dropdb():
    db.drop_all()
    return 'drop_table'


 

################################################
#################### view site #################
################################################

@app.route("/")
def hello():
    return render_template('index.html', title="Welcome")

@app.route("/tipos")
def tipos():
    registros = Tipos.query.filter(Tipos.id > 0) \
        .order_by(Tipos.descricao.desc()).limit(4)
    return render_template('tipos.html', rows=registros , title="Tipos")
 



################################################
#################### api rest  #################
################################################
@app.route("/api/tipos")
def tipos_api():
    users = Tipos.query.all()
    return jsonify([user.descricao for user in users])

@app.route('/api/tipos/add', methods=['POST'])
def new(): 
    content = request.json 
    try:
        if request.method == 'POST':
            descricao = content['descricao']
            todo = Tipos(descricao)
            db.session.add(todo)
            db.session.commit()
            MESSAGE = f"Tipos {descricao} successfully updated"
            RESULT = True
    except Exception as error:
        MESSAGE = f"Ops :) {error}"
        RESULT  = False
    return jsonify({ 'success': RESULT , 'message': MESSAGE })


@app.route('/api/estados/add', methods=['POST'])
def estado_create():
    content = request.json
    try:
        if request.method == 'POST':
            sigla = content['Sigla']
            nome = content['Nome']
            # Check that email does not already exist (not a great query, but works)
            #if not db.session.query(Estados).filter(nome == nome).count():
            reg = Estados(sigla, nome)
            db.session.add(reg)
            db.session.commit()
            MESSAGE = f"Estados {nome} successfully updated"
            RESULT = True
    except Exception as error:
        print(error)
        #raise  
        MESSAGE = f"Ops :) {error}"
        RESULT = False
    
    return jsonify({'success': RESULT , 'message': MESSAGE }) 

@app.route("/api/estados")
def estado_lista():
    try:
        #User.query.filter_by(username=username).first_or_404(description='There is no data with {}'.format(username))
        users = Estados.query.all()
        RESULT = True
        MESSAGE = ""
        return jsonify({
            'success': RESULT,
            'rows': users,
            'message': MESSAGE 
        }) 
        
        #return jsonify([user.descricao for user in users])
    except Exception as error:
        MESSAGE = f"Ops :) {error}"
        RESULT = False
        return jsonify({ 'success': RESULT, 'rows': None, 'message': MESSAGE }) 
```


# Development

   - Axel Alexander

# My web site

- [My Homepage](https://axe-dev.herokuapp.com/)

<p align="center">
    <a href="https://github.com/axeldeveloper">
        <img title="Author" 
            src="https://img.shields.io/badge/AUTHOR-AXEL-orange.svg?style=for-the-badge&logo=github">
    </a>
</p>


<p align="center">
    <a href="https://www.linkedin.com/in/axeldeveloper/">
        <img title="Linkedin" 
        src="https://img.shields.io/badge/LINKDIN-AXEL-blue.svg?style=for-the-badge&logo=linkedin">
    </a>
</p>


# Contributing

- Axel
- anomimous


# Versioning

# Authors

 Axel Alexander  - [contact and contracts](http://axel-dev.herokuapp.com/)

  | Front | HTML | CSS    | VueJS | React | React |
  | ----- | ---- | ------ | ----- | ----- | ----- |
  | Back  | C#   | Python | Ruby  | Go    | PHP   |



See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.


# License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details