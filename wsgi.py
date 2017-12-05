from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "Conectando Flask SQLAlchemy POSTGRESS!"

@application.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)



if __name__ == "__main__":
    application.run()
