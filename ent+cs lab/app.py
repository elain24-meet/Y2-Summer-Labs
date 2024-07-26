
from flask import Flask, render_template, url_for, redirect, request
from flask import session as login_session
import pyrebase


 
app = Flask(__name__, template_folder='templates', static_folder='static')

app.config['SECRET_KEY'] = 'super-secret-key'

config = {
  "apiKey": "AIzaSyDf8OnDIHYzz-ycd143ZkcVmD-K9ictuQw",
  "authDomain": "auth-lab-53325.firebaseapp.com",
  "projectId": "auth-lab-53325",
  "storageBucket": "auth-lab-53325.appspot.com",
  "messagingSenderId": "140295796023",
  "appId": "1:140295796023:web:11130be94a50c70ef516b2",
  "measurementId": "G-TM23J59KMQ",
  "databaseURL":"https://auth-lab-53325-default-rtdb.europe-west1.firebasedatabase.app/"
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db =firebase.database()



if __name__ == '__main__':
 
    app.run( debug=True)