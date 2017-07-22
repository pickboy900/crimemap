import dbconfig
if dbconfig.test:
	from mockdbhelper import MockDBHelper as DBHelper
else:
	from dbhelper import DBHelper
from flask import Flask, render_template, request, json, redirect, url_for

app = Flask(__name__)
DB = DBHelper()

@app.route('/')
def home():
	crimes = DB.get_all_crimes()
	crimes = json.dumps(crimes)
	return render_template('home.html', crimes=crimes)

@app.route("/submitcrime", methods=["POST"])
def submitcrime():
	form_keys = request.form
	for var in form_keys:
		globals()[var] = request.form.get(var)
	DB.add_crime(date, category, description, longitude, latitude)
	return redirect(url_for('home'))
	
if __name__=='__main__':
	app.run(port=500, debug=True)