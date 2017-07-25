import os

DB_USERNAME = '<db user>'
DB_PASSWORD = '<db pwd>'
DB_DATABASE_NAME = 'shortener'
DB_HOST = os.getenv('IP', '127.0.0.1')
APPLICATION_DIR = os.path.dirname(os.path.realpath(__file__))
SQLALCHEMY_TRACK_MODIFICATIONS = True
DEBUG = True
SECRET_KEY = '<$üP3rPazzwø£D>'
SQLALCHEMY_DATABASE_URI = "mysql+pymysql://%s:%s@%s/%s" % (DB_USERNAME, DB_PASSWORD, DB_HOST, DB_DATABASE_NAME)
STATIC_DIR = os.path.join(APPLICATION_DIR, 'static')
RECAPTCHA_PUBLIC_KEY = '<Your own keys from Google>'
RECAPTCHA_PRIVATE_KEY = '<You can get these keys at https://www.google.com/recaptcha/admin>'
RECAPTCHA_DATA_ATTRS = {'theme': 'dark'}
SERVER_NAME = 'localhost:5000'
# SERVER_NAME = 'YourDomain.com'
