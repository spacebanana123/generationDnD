from flask import Flask
app = Flask(__name__)

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
