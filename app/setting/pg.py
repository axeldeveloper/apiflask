POSTGRES = {
    'user': 'anonimous',
    'pw': 'anonimous',
    'db': 'tarefa_api',
    'host': 'flask_api_db',
    'port': '5432',
}

DATABASE_URI = "postgresql+psycopg2://anonimous:anonimous@flask_api_db:5432/tarefa_api"
SQLALCHEMY_DATABASE_URI = DATABASE_URI
SQLALCHEMY_ECHO = False
SECRET_KEY = '\xfb\x12\xdf\xa1@i\xd6>V\xc0\xbb\x8fp\x16#Z\x0b\x81\xeb\x16'
SQLALCHEMY_TRACK_MODIFICATIONS = True
DEBUG = True
PROPAGATE_EXCEPTIONS = True
