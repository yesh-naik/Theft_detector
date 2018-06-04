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
    MAILGUN_API_KEY = '8bd85a46e3e3f771a05ea7e570c14b4c-b6183ad4-2682a351'
    SANDBOX_URL= 'sandboxaf5eede11d354bb089250cd53c2ff34e.mailgun.org'
    SENDER_EMAIL = 'yeshwant_naik@sandboxaf5eede11d354bb089250cd53c2ff34e.mailgun.org'
    RECIPIENT_EMAIL = 'yeshwantnaik12@gmail.com'
    API_KEY = '5c13db10-a9f9-4d67-9fff-f03a0b13288f'
    DEVICE_ID  = 'BOLT3622826'
