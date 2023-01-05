from dndGen import classes, races, rollChar
from flask import Flask, render_template
from dndEncouter import genEnc, randEnc
from dndCampaign import makeCampaign
from dndQuest import genQuest
from dndTraps import genTrap
import random


app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/luckynumber')
def luckNum():
  luckyNumbers = ""
  for i in range(7):
    rand = random.randint(0,100)
    luckyNumbers += str(rand)
    luckyNumbers += " "
  return render_template('luckyNumber.html', luckyNumbers = luckyNumbers)

@app.route("/dndgen")
def dndGen():
  char = rollChar()
  return render_template("dndGen.html", char = char)

@app.route("/randomencounter")
def dndEncounter(): 
  other, easy, med, hard = genEnc()
  encounter = randEnc()
  return render_template("randEnc.html", other = other, easy = easy, med = med, hard = hard, encounter = encounter)

@app.route("/randomcampaign")
def dndCampaign():
  camp = makeCampaign()
  return render_template("makeCamp.html", camp = camp)

@app.route("/randomquest")
def makeQuest():
  quest = genQuest()
  return render_template("makeQuest.html", quest = quest)

@app.route("/randomtraps")
def makeTrap():
  trap = genTrap()
  return render_template("randomTraps.html", trap = trap)
    
