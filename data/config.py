import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = str(os.getenv('BOT_TOKEN')) #Токен бота в файле .env

admins = [
    6109859293 #admin
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'myStomadb',
        'USER': 'root',
        'PASSWORD': 'sabitov2006',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}