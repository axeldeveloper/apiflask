from flask import Flask, jsonify
from app.setting.db import db
from app.rest.table import table
from dotenv import dotenv_values
from flask_migrate import Migrate


#from app.setting.pg import SQLALCHEMY_DATABASE_URI


config = dotenv_values(".env")

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = config['DATABASE_URL']
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#app.config['DEBUG'] = True
app.config['FLASK_DEBUG'] = True


db.init_app(app)

migrate = Migrate(app, db, compare_type=True)
#manager = Manager(app)
#manager.add_command('db', MigrateCommand)

app.register_blueprint(table)

@app.errorhandler(500)
@app.errorhandler(404)
def not_found_error(ex):
    return jsonify(error=str(ex)), ex.code

@app.route("/")
def hello_world():
    return jsonify(msg="Welcome 45", db=config['DATABASE_URL'] , config=config)



if __name__ == "__main__":
    app.run()