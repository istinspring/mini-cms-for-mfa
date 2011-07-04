import os.path as op
from settings import PROJECT_ROOT


DEBUG = True
TEMPLATE_DEBUG = DEBUG

DB_PATH = op.join(PROJECT_ROOT, 'db')

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': op.join(DB_PATH, 'data.sqlite'),
    }
}

SECRET_KEY = '9@-a*+d1ms+25q8h83zjkym=qs$rtdn5i!aqszd$buo5*3mky-'
