
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

#new user
@app.route('/', methods=['GET', 'POST'])
def signup():
  if request.method == 'GET':
    return render_template("signup.html")
  else:
      email = request.form['Email']
      password = request.form['Password']
      full_name = request.form['Full_name']
      username = request.form['Username']
      try:
        login_session['quotes'] = []
        login_session['user'] = auth.create_user_with_email_and_password(email, password)
        user = {"Full_name": full_name,"Email": email ,"Username": username}
        UID = login_session['user']['localId']
        db.child("Users").child(UID).set(user)

        return redirect(url_for('home'))
      except:
        print("error")
        return render_template("signup.html")


@app.route('/home', methods=['GET', 'POST'])
def home():
  if request.method == 'GET':
    return render_template("home.html")
  else:
      quote1 = request.form['Quote']
      nameQ = request.form['NameQ']
      try:
        quote={
        "text": quote1,
        "said_by": nameQ,
        "uid": login_session['user']['localId'],
        "qoute": quote1
        }
        db.child("Quotes").push(quote)
        return redirect(url_for('thanks'))
      except:
        print("error")


@app.route('/signout')
def signout():
  login_session['user'] = None
  auth.current_user = None
  return redirect(url_for('signin'))

   
#exict user
@app.route('/signin', methods=['GET', 'POST'])
def signin():
  if request.method == 'GET':
    return render_template("signin.html")
  else:
    email = request.form['Email']
    password = request.form['Password']
    
    try:
      login_session['User'] = auth.sign_in_with_email_and_password(email, password)
     

      return redirect(url_for('home'))
    except Exception as e:
      print(e)


@app.route('/display', methods=['GET', 'POST'])
def display():
    
    return render_template("display.html" , quotes=db.child("Quotes").get().val()) 


@app.route('/thanks', methods=['GET', 'POST'])
def thanks():
  if request.method == 'GET]':

    return render_template("thanks.html")
  else:
    return render_template("thanks.html")

if __name__ == '__main__':
 
    app.run( debug=True)