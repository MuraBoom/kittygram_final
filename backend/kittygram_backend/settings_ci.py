# settings_ci.py - для тестов CI
from .settings import *

# SQLite для тестов
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',  # в памяти, не создаёт файл
    }
}

SECRET_KEY = 'test-secret-key-ci-123456'

# Отключаем все проверки требующие БД
SILENCED_SYSTEM_CHECKS = ['*']
