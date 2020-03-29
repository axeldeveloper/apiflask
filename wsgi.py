
import os

from flask import Flask, request, render_template, redirect, url_for , flash ,json , jsonify 

from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from config import CONECTION_STRING , DEBUG, RESULT, MESSAGE

################################################
#################### config ####################
################################################

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = CONECTION_STRING
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['DEBUG'] = DEBUG


db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

from models import Tipos, Estados


################################################
#################### db     ####################
################################################

@app.route('/create_table/')
def create_table():
    db.create_all()
    return 'create_table'
    
@app.route('/drop_table/')
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
 
@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), 500


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
        return jsonify({ 'success': RESULT, 'rows': users 'message': MESSAGE }) 
        #return jsonify([user.descricao for user in users])
    except Exception as error:
        MESSAGE = f"Ops :) {error}"
        RESULT = False
        return jsonify({ 'success': RESULT, 'rows': None, 'message': MESSAGE }) 





if __name__ == "__main__":
    app.run()
