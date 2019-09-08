
from flask import Flask, request, render_template, redirect, url_for , flash

from flask_sqlalchemy import SQLAlchemy


from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask import json
from flask import jsonify 
import os

from config import CONECTION_STRING

#from models import Tipos

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = CONECTION_STRING

# application.config.from_pyfile('alphonce.cfg')
# application.config['PROPAGATE_EXCEPTIONS'] = True
# application.config['SQLALCHEMY_DATABASE_URI'] = os.environ['OPENSHIFT_POSTGRESQL_DB_URL']
# application.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:766312@localhost/flask'
# application.config['SQLALCHEMY_DATABASE_URI'] = os.environ['OPENSHIFT_POSTGRESQL_DB_URL']
# SQLALCHEMY_DATABASE_URI = os.environ['OPENSHIFT_POSTGRESQL_DB_URL']
 # SQLALCHEMY_ECHO = False

app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

app.config['DEBUG'] = True

#application.secret_key = '\xfb\x12\xdf\xa1@i\xd6>V\xc0\xbb\x8fp\x16#Z\x0b\x81\xeb\x16'



db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

from models import Tipos

@app.route("/")
def hello():
    return render_template('index.html', title="Welcome")

@app.route("/api/tipos")
def tipos_api():
    users = Tipos.query.all()
    return jsonify([user.descricao for user in users])

@app.route("/tipos")
def tipos():
    registros = Tipos.query.filter(Tipos.id > 0) \
        .order_by(Tipos.descricao.desc()).limit(4)
    return render_template('tipos.html', rows=registros , title="Tipos")
 
  
"""
@application.route('/tipos/add', methods=['GET', 'POST'])
def new():
    if request.method == 'POST':
            todo = models.Tipos(request.form['email'])
            db.session.add(todo)
            db.session.commit()
            return redirect(url_for('index'))
    return render_template('new.html')
"""


# Save e-mail to database and send to success page
"""
@application.route('/prereg', methods=['POST'])
def prereg():
    email = None
    if request.method == 'POST':
    email = request.form['email']
    # Check that email does not already exist (not a great query, but works)
    if not db.session.query(User).filter(User.email == email).count():
        reg = User(email)
        db.session.add(reg)
        db.session.commit()
        return render_template('success.html') 
    return render_template('index.html')
"""




if __name__ == "__main__":
    application.run()
