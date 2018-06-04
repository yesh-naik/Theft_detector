Note: starting a new virtual python env is highly recommended

Below command will install all the required packages. [More than required to be frank :P]
pip install -r requirements.txt

Please export below parameters in your environment so that config.py file picks them up correctly

SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
MAIL_SERVER = smtp.googlemail.com
MAIL_PORT = 587
MAIL_USE_TLS = 1
MAIL_USERNAME = os.environ.get('MAIL_USERNAME') #your gmail_id
MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD') #your gmail_pass
ADMINS = ['yeshwantnaik12@gmail.com'] #your gmail_id
MAILGUN_API_KEY = os.environ.get('MAILGUN_API_KEY') #ignore/remove from config.py 
SANDBOX_URL= os.environ.get('SANDBOX_URL')    #ignore/remove from config.py
SENDER_EMAIL = os.environ.get('SENDER_EMAIL') 
RECIPIENT_EMAIL = os.environ.get('RECIPIENT_EMAIL')
API_KEY = os.environ.get('API_KEY') #your BOLT api key
DEVICE_ID  = os.environ.get('DEVICE_ID') #your device id
