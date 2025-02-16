import os
import string


USER_LINK_LIMIT = 16
VALID_SYMBOLS = string.ascii_letters + string.digits
INVALID_SYMBOLS = (f'Введены недопустимые символы.'
                   f'Разрешенные символы: {VALID_SYMBOLS}')


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI')
    SECRET_KEY = os.getenv('SECRET_KEY')