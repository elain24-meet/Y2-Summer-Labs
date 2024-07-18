from flask import Flask, render_template, url_for, redirect, request
from flask import session as login_session
app = Flask(__name__,
template_folder="templates",
static_folder='static')


app.config['SECRET_KEY'] = "Your_secret_string"


@app.route('/loggin',methods=['GET','POST'])
def loggin():
	if request.method == 'GET':
		return render_template('loggin.html')
	else:
		usersname = request.form['Usersname'] 
		birthMonth = request.form['BirthMonth'] 
		login_session['Usersname'] = usersname   
		
		return render_template('home.html',userN=usersname ,birthM=birthMonth)

# @app.route('/home',methods=['GET','POST'])
# def home():
# 	if request.method == 'GET':
# 		return render_template('home.html')
# 	else:
# 		 userN =
# 		return redirect(url_for('home',birthM=birthMonth))

@app.route('/fortune/<birthM>')
def fortune(birthM):
	possible_fortunes = ["Be careful or you could fall for some tricks today.", "A beautiful, smart, and loving person will be coming into your life.",
	"A fresh start will put you on your way.", "A truly rich life contains love and art in abundance.",
	"A short pencil is usually better than a long memory any day.", "At the touch of love, everyone becomes a poet.", 
	"An important person will offer you support.", "Better ask twice than lose yourself once.", "An inch of time is an inch of gold.",
	"Bide your time, for success is near."]
	lenOfMonth = len(birthM)
	finalFortune = possible_fortunes[9]
	if lenOfMonth < 10:
		finalFortune = possible_fortunes[lenOfMonth-1]
	else:
		finalFortune = "Not availible"
	return render_template("fortune.html", fortune = finalFortune)


if __name__ == '__main__':
    app.run(debug = True)