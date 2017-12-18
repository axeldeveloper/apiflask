#################
#### imports ####
#################
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
#from models import Tipos


################
#### config ####
################


application = Flask(__name__)
application.config['DEBUG'] = True
application.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:766312@localhost/flask'
application.secret_key = 'some_secret'
#application.config.from_pyfile('alphonce.cfg')
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(application)

import models

@application.route("/")
def hello():
    #return "Conectando Flask SQLAlchemy POSTGRESS!"
    all_public_recipes = models.Tipos.query.filter(
        models.Tipos.Id > 0)\
        .order_by(models.Tipos.Descricao.desc()).limit(4)
    return render_template('index.html', rows=all_public_recipes)
    #return render_template('index.html')


# Save e-mail to database and send to success page
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


@application.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)



if __name__ == "__main__":
    application.run()
