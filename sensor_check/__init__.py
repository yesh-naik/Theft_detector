import os
from flask import Flask
from flask_mail import Mail
from config import Config
from boltiot import Bolt

app = Flask(__name__)
app.config.from_object(Config)
mail = Mail(app)



if not app.debug and not app.testing:
        if app.config['MAIL_SERVER']:
            auth = None
            print(app.config['MAIL_SERVER'])
            if app.config['MAIL_USERNAME'] or app.config['MAIL_PASSWORD']:
                auth = (app.config['MAIL_USERNAME'],
                        app.config['MAIL_PASSWORD'])
            secure = None
            
from sensor_check import routes

