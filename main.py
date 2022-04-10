
from flask import Flask, jsonify
from config import CONECTION_STRING

from app.rest.table import table
from db import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = CONECTION_STRING
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['DEBUG'] = True
db.init_app(app)
app.register_blueprint(table)

@app.errorhandler(500)
@app.errorhandler(404)
def not_found_error(ex):
    return jsonify(error=str(ex)), ex.code

@app.route("/")
def hello_world():
    return jsonify(msg="Welcome")



if __name__ == "__main__":
    app.run()