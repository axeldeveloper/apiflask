import os

workers = int(os.environ.get('GUNICORN_PROCESSES', '3'))
threads = int(os.environ.get('GUNICORN_THREADS', '1'))

forwarded_allow_ips = '*'
secure_scheme_headers = { 'X-Forwarded-Proto': 'https' }

POSTGRES = {
    'user': 'postgres',
    'pw': '766312',
    'db': 'tarefa_api',
    'host': 'localhost',
    'port': '15432',
}

CONECTION_STRING = 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES


#SQLALCHEMY_DATABASE_URI = 'postgresql://%(user)s:\%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
SQLALCHEMY_DATABASE_URI    = 'sqlite:////tmp/test.db'
SQLALCHEMY_DATABASE_SQLITE = 'sqlite:////tmp/test.db'
SQLALCHEMY_DATABASE_PG     ='postgresql://localhost/flask'
SQLALCHEMY_ECHO = False
SECRET_KEY = '\xfb\x12\xdf\xa1@i\xd6>V\xc0\xbb\x8fp\x16#Z\x0b\x81\xeb\x16'
SQLALCHEMY_TRACK_MODIFICATIONS = True
DEBUG = True
PROPAGATE_EXCEPTIONS = True


# application.config.from_pyfile('flask.cfg')
# application.config['PROPAGATE_EXCEPTIONS'] = True
# application.config['SQLALCHEMY_DATABASE_URI'] = os.environ['OPENSHIFT_POSTGRESQL_DB_URL']
# application.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:766312@localhost/flask'
# application.config['SQLALCHEMY_DATABASE_URI'] = os.environ['OPENSHIFT_POSTGRESQL_DB_URL']


LANGUAGES = {
   'en': {'flag':'gb', 'name':'English'},
   'pt': {'flag':'pt', 'name':'Portuguese'}
}

RESULT = None

MESSAGE == ''