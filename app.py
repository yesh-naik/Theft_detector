from flask import Flask, render_template, request,json
from boltiot import Bolt
api_key = "5c13db10-a9f9-4d67-9fff-f03a0b13288f"
device_id  = "BOLT3622826"
mybolt = Bolt(api_key, device_id)

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    print(request.method)
    if request.method == 'POST':
        if request.form.get('Encrypt') == 'Encrypt':
            # pass
            print("Encrypted")
        elif  request.form.get('Decrypt') == 'Decrypt':
            # pass # do something else
            print("Decrypted")
        else:
            # pass # unknown
            return render_template("index.html")
    elif request.method == 'GET':
        # return render_template("index.html")
        print("No Post Back Call")
    return render_template("index.html")


if __name__ == '__main__':
    app.run()