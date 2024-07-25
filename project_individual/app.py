
from flask import Flask, render_template, url_for, redirect, request
from flask import session as login_session
import pyrebase


 
app = Flask(__name__, template_folder='templates', static_folder='static')

app.config['SECRET_KEY'] = 'super-secret-key'


config = {
  'apiKey': "AIzaSyB7spmSsMk_wtaGWaF4hkhl2iyJfFen6eE",
  'authDomain': "individual-596de.firebaseapp.com",
  'projectId': "individual-596de",
  'storageBucket': "individual-596de.appspot.com",
  'messagingSenderId': "787133005211",
  'appId': "1:787133005211:web:48ab45474f5aff8fecb53e",
  'measurementId': "G-QVLWG3KJFY",
  "databaseURL":"https://individual-596de-default-rtdb.europe-west1.firebasedatabase.app/"
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db =firebase.database()


#new user 
#SIGN UP

@app.route('/', methods=['GET', 'POST'])
def signup():
  if request.method == 'GET':
    return render_template("signup.html")
  else:
      email = request.form['Email']
      password = request.form['Password']
      username = request.form['Username']
      try:
        login_session['user'] = auth.create_user_with_email_and_password(email, password)
        user = {"Email": email ,"Username": username}

        UID = login_session['user']['localId']
        db.child("Users").child(UID).set(user)
        return redirect(url_for('type'))
      except Exception as e:
        print(e)
        return render_template("signup.html")




#exict user
#SIGN IN

@app.route('/signin', methods=['GET', 'POST'])
def signin():
  if request.method == 'GET':
    return render_template("signin.html")
  else:
    email = request.form['Email']
    password = request.form['Password']
    
    try:
      login_session['User'] = auth.sign_in_with_email_and_password(email, password)
      return redirect(url_for('type'))
    except:
        print("error sign in")
        return render_template("signin.html")

    #SIGN OUT

#@app.route('/signout')
#def signout():
 # login_session['user'] = None
  #auth.current_user = None
 # return redirect(url_for('signin'))
  #    return redirect(url_for('home'))
   # except Exception as e:
    #  print(e)


#ABOUT

@app.route('/about', methods=['GET', 'POST'])
def about():
  return render_template("about.html")



#TYPE

@app.route('/type', methods=['GET', 'POST'])
def type():
  if request.method == 'GET':
    return render_template("type.html")
  else:
      typeOfHair = request.form['type']
        
      if request.form['type'] == "Curly":
        return render_template("curly.html")
      if request.form['type'] == "Wavy":
        return render_template("wavy.html")
      if request.form['type'] == "Straigth":
        return render_template("straigth.html")
      if request.form['type'] == "Combination":
        return render_template("combination.html")


      return render_template("type.html")
   



#CURLY HAIR

@app.route('/curly', methods=['GET', 'POST'])
def curly():
  if request.method == 'GET]':
    return render_template("curly.html")
  else:
      if request.form['typeCu'] == "Loose":
        return redirect(url_for('result',Hairtype='curly',subtype='loose'))
      if request.form['typeCu'] == "Medium":
        return redirect(url_for('result',Hairtype='curly',subtype='medium'))
      if request.form['typeCu'] == "Tight":
        return redirect(url_for('result',Hairtype='curly',subtype='tight'))



    #COMBINATION HAIR

@app.route('/combination', methods=['GET', 'POST'])
def combination():
  if request.method == 'GET]':
    return render_template("combination.html")
  else:
      if request.form['typeCo'] == "Oily&Dry":
        return redirect(url_for('result',Hairtype='combination',subtype='oilydry'))
      if request.form['typeCo'] == "Dry&Oily":
        return redirect(url_for('result',Hairtype='combination',subtype='dryoily'))


#STRAIGTH HAIR

@app.route('/straigth', methods=['GET', 'POST'])
def straigth():
  if request.method == 'GET]':
    return render_template("straigth.html")
  else:
      if request.form['typeS'] == "Fine":
        return redirect(url_for('result',Hairtype='straight',subtype='fine'))
      if request.form['typeS'] == "Thick":
        return redirect(url_for('result',Hairtype='straight',subtype='thick'))


#WAVY HAIR

@app.route('/wavy', methods=['GET', 'POST'])
def wavy():
  if request.method == 'GET]':
    return render_template("wavy.html")
  else:

      if request.form['typeW'] == "Loose":
        return redirect(url_for('result',Hairtype='wavy',subtype='loose'))
      if request.form['typeW'] == "Medium":
        return redirect(url_for('result',Hairtype='wavy',subtype='medium'))
      if request.form['typeW'] == "Tight":
        return redirect(url_for('result',Hairtype='wavy',subtype='tight'))
    


#RESULT

@app.route('/result/<Hairtype>/<subtype>', methods=['GET', 'POST'])
def result(Hairtype, subtype):
  info = db.child("Hair types").child(Hairtype).child(subtype).get().val()
  likes = info['likes']
  dislikes = info['dislikes']
  links = info['links']
  if request.method == 'GET':
      db.child("Hair types").child(Hairtype).child(subtype).get().val()
      return render_template("result.html",links = links, hairtype = Hairtype, subtype = subtype, likes = likes, dislikes = dislikes)
  else:
      action = request.form['action']
      
      
      if action == 'like':
          likes += 1
          db.child("Hair types").child(Hairtype).child(subtype).update({"likes": likes})
      elif action == 'dislike':
          dislikes += 1
          db.child("Hair types").child(Hairtype).child(subtype).update({"dislikes": dislikes})
      
      return redirect(url_for('result', Hairtype=Hairtype, subtype=subtype))



if __name__ == '__main__':
 
    app.run( debug=True)