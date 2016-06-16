from WebApp.settings.base import *

print('os.environ : ', os.environ)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ['MYSQL_DATABASE'],
        'USER': os.environ['MYSQL_USER'],
        'PASSWORD': os.environ['MYSQL_PASSWORD'],
        'HOST': os.environ['MYSQL_CONTAINER_NAME'],
        'PORT': os.environ['MYSQL_PORT']
    }
}

