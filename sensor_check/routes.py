from flask import render_template,request,flash
from sensor_check import app
from boltiot import Bolt
import json,time
from threading import Thread
from multiprocessing import Process,current_process
from flask_mail import Message
from flask import render_template
from sensor_check import mail
from boltiot import Email
from config import Config
import datetime 

app.config.from_object(Config)

API_KEY = app.config['API_KEY']
DEVICE_ID  = app.config['DEVICE_ID']
mybolt = Bolt(API_KEY, DEVICE_ID)


MAILGUN_API_KEY = app.config['MAILGUN_API_KEY']
SANDBOX_URL= app.config['SANDBOX_URL']
SENDER_EMAIL = app.config['SENDER_EMAIL']
RECIPIENT_EMAIL = app.config['RECIPIENT_EMAIL']
senders=app.config['ADMINS'][0]
now=datetime.datetime.now()





def send_mail():
        sub='Burglar Alert at: ' + now.strftime("%Y-%m-%d %H:%M") + '!!!!'
        mailer = Email(MAILGUN_API_KEY, SANDBOX_URL, SENDER_EMAIL, RECIPIENT_EMAIL) # Create object to send Email
        mailer.send_email(sub, "Dear User, \n\nWe have detected intruder movement in your vault!! \n\nTo stop the buzzing alarm at your premises, <a href='https://cloud.boltiot.com/remote/5c13db10-a9f9-4d67-9fff-f03a0b13288f/digitalWrite?pin=1&state=LOW&deviceName=BOLT3622826'> click here </a> . Please take required action immediately. \n\nSincerely, \n\nBolt Team")

def send_email():
        with app.app_context():   
                msg = Message('Burglar Alert at: ' + now.strftime("%Y-%m-%d %H:%M") + '!!!!', sender=senders,recipients=['yeshwantnaik12@gmail.com'])
                msg.body = "Dear User, \nWe have detected intruder movement in your vault!! \nTo stop the buzzing alarm at your premises, href='https://cloud.boltiot.com/remote/5c13db10-a9f9-4d67-9fff-f03a0b13288f/digitalWrite?pin=1&state=LOW&deviceName=BOLT3622826' . \n Please take required action immediately. \nSincerely, \nBolt Team"
                msg.html = "<p>Dear User,</p> \n<p>We have detected intruder movement in your vault!!</p> \n <p>To stop the buzzing alarm at your premises, <a href='https://cloud.boltiot.com/remote/5c13db10-a9f9-4d67-9fff-f03a0b13288f/digitalWrite?pin=1&state=LOW&deviceName=BOLT3622826'> click here </a>. \n<p>Please take required action immediately </p> \n\n<p>Sincerely,</p> \n<p>Bolt Team</p>"
                mail.send(msg)


# class start_sensor(Thread):
#         def __init__(self):
#                 Thread.__init__(self,name="t_sense")
#                 self.daemon = True
#                 self.start()

#         def run(self):
#                 while(1):
#                         inp=mybolt.analogRead('A0')
#                         val=json.loads(inp)
#                         v=val["value"]
#                         if (int(val["success"]) == 1):
#                                 if ( int(v) < 1000 ):
#                                         mybolt.digitalWrite(1,'HIGH')
#                                         send_mail()
#                                         send_email()
#                                         print('Motion detected!!!')
#                                         break
#         def status_chk(self):
#                 return self.is_alive()

#         def cancel(self):
#                 self.cancelled = True



def sensor():
        while(1):
                inp=mybolt.analogRead('A0')
                val=json.loads(inp)
                v=val["value"]
                print (int(v))
                #print(SENSOR_FLAG)
                if (SENSOR_FLAG == 1):
                        print('Stopping the sensor!!')
                        break
                if (int(val["success"]) == 1):
                        if ( int(v) < 1000 ):
                                mybolt.digitalWrite(1,'HIGH')

                                print('Motion detected!!!')
                                #send_mail()
                                send_email()
                                break
                else:
                        print('Failure')
                ##Sleep added to avoid overloading system
                time.sleep(5)
                
sense=Thread(target=sensor)

def restart_thread():
        print('thread restarted')
        sense=Thread(target=sensor)

@app.route('/',methods=['GET', 'POST'])
@app.route('/index',methods=['GET', 'POST'])
def index():
        if request.method == 'POST':

                if request.form.get('start_sensor') == 'start_sensor':
                        #start_sensor()
                        try:
                                # if (sense.is_alive == 'False'):
                                #         sense=Thread(target=sensor)
                                #         sense.start()
                                global SENSOR_FLAG
                                SENSOR_FLAG=0
                                sense.daemon= True
                                sense.start()
                                print('sensor started')
                                
                        except RuntimeError:
                                print('Thread ka problem')
                                
                                

                elif  request.form.get('alarm_stop') == 'alarm_stop':
                        mybolt.digitalWrite(1,'LOW')
                        print('Alarm stopped !!!')
                elif  request.form.get('stop_sensor') == 'stop_sensor':
                        try:
                                SENSOR_FLAG=1
                                print(SENSOR_FLAG)
                                sense.join()
                        except RuntimeError:
                                print('Thread not yet started')
                elif  request.form.get('refresh_sensor_status') == 'refresh_sensor_status':
                        print(sense.is_alive())
                else:
                        return render_template("index.html")

                if (sense.is_alive()):
                        color="green"
                else:
                        color="red"

        elif request.method == 'GET':
                print("No Post Back Call")
                color="red"
        return render_template('index.html', title='Home',status=color)
