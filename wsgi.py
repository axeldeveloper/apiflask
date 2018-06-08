#################
#### imports ####
#################
from flask import Flask, render_template, request, flash, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
import os

#from models import Tipos


################
#### config ####
################


application = Flask(__name__)


#application.config.from_pyfile('alphonce.cfg')

application.config['PROPAGATE_EXCEPTIONS'] = True
#application.config['SQLALCHEMY_DATABASE_URI'] = os.environ['OPENSHIFT_POSTGRESQL_DB_URL']
#application.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:766312@localhost/flask'
application.config['SQLALCHEMY_DATABASE_URI'] = os.environ['OPENSHIFT_POSTGRESQL_DB_URL']
#SQLALCHEMY_DATABASE_URI = os.environ['OPENSHIFT_POSTGRESQL_DB_URL']
#SQLALCHEMY_ECHO = False
application.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

application.config['DEBUG'] = True

application.secret_key = '\xfb\x12\xdf\xa1@i\xd6>V\xc0\xbb\x8fp\x16#Z\x0b\x81\xeb\x16'

db = SQLAlchemy(application)

import models

@application.route("/")
def hello():
    return render_template('index.html', title="Welcome")




@application.route("/tipos")
def tipos():
    #return "Conectando Flask SQLAlchemy POSTGRESS!"
    registros = models.Tipos.query.filter(
        models.Tipos.Id > 0)\
        .order_by(models.Tipos.Descricao.desc()).limit(4)
    return render_template('tipos.html', rows=registros , title="Tipos")
    #return render_template('index.html')

@application.route('/tipos/add', methods=['GET', 'POST'])
def new():
    if request.method == 'POST':
            todo = models.Tipos(request.form['email'])
            db.session.add(todo)
            db.session.commit()
            return redirect(url_for('index'))
    return render_template('new.html')



# Save e-mail to database and send to success page

@application.route('/prereg', methods=['POST'])
def prereg():
    email = None
    """ if request.method == 'POST':
    email = request.form['email']
    # Check that email does not already exist (not a great query, but works)
    if not db.session.query(User).filter(User.email == email).count():
        reg = User(email)
        db.session.add(reg)
        db.session.commit()
        return render_template('success.html') """
    return render_template('index.html')



@application.route('/test/<name>')
def hello_name(name):
    return "Hello {}!".format(name)






if __name__ == "__main__":
    application.run()
