from flask import Flask
import pandas as pd


app = Flask(__name__)
 
@app.route("/")
def load_data():

	return part_db.to_html()

@app.route("/year/<y>")
def year_filter(y):
	y = str(y)
	year_filtered = sentence_db[(sentence_db['Year'].astype(str)== y)]
	
	return  year_filtered.to_html()

@app.route("/candidate/<c>")
def candidate_filter(c):
	
	candidate_filtered = sentence_db[(sentence_db['Speaker'].astype(str)== c.lower())]
	
	return  candidate_filtered.to_html()

@app.route("/hello")
def hello():
	return "Hello World!"
 


 
if __name__ == "__main__":
	token_db =  pd.read_csv("data/token_db_candidate.csv")
	sentence_db =  pd.read_csv("data/sentence_db_candidate.csv")
	part_db =  pd.read_csv("data/part_db_candidate.csv")
	
	app.run()
