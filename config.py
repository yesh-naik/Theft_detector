import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['yeshwantnaik12@gmail.com']
    MAILGUN_API_KEY = os.environ.get('MAILGUN_API_KEY')
    SANDBOX_URL= os.environ.get('SANDBOX_URL')    
    SENDER_EMAIL = os.environ.get('SENDER_EMAIL') 
    RECIPIENT_EMAIL = os.environ.get('RECIPIENT_EMAIL')
    API_KEY = os.environ.get('API_KEY')
    DEVICE_ID  = os.environ.get('DEVICE_ID')
