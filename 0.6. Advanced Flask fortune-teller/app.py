from flask import Flask, render_template
import random
app = Flask(__name__,
template_folder="templates",
static_folder='static')

@app.route('/home')
def home():
    return render_template(
	"home.html")

@app.route('/fortune')
def fortune():
	possible_fortunes = ["Be careful or you could fall for some tricks today.", "A beautiful, smart, and loving person will be coming into your life.",
	"A fresh start will put you on your way.", "A truly rich life contains love and art in abundance.",
	"A short pencil is usually better than a long memory any day.", "At the touch of love, everyone becomes a poet.", 
	"An important person will offer you support.", "Better ask twice than lose yourself once.", "An inch of time is an inch of gold.",
	"Bide your time, for success is near."]
	random.randint(1,11)
	rand_fortune = random.choice(possible_fortunes)
	return render_template("fortune.html", rand_fortune = rand_fortune)


if __name__ == '__main__':
    app.run(debug = True)