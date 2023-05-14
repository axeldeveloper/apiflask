import os

workers = int(os.environ.get('GUNICORN_PROCESSES', '3'))
threads = int(os.environ.get('GUNICORN_THREADS', '1'))

forwarded_allow_ips = '*'
secure_scheme_headers = { 'X-Forwarded-Proto': 'https' }

LANGUAGES = {
   'en': {'flag':'gb', 'name':'English'},
   'pt': {'flag':'pt', 'name':'Portuguese'}
}

RESULT = ""

MESSAGE = 'Created'