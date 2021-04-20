from flask import Flask, render_template, flash, request
#from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from flask_bootstrap import Bootstrap
import pandas as pd
from  classifier import Model
from string import punctuation
from nltk.tokenize import word_tokenize,sent_tokenize
import createChat
import json
from flask import jsonify
from waitress import serve



# App config.
#DEBUG = True
app = Flask(__name__)
Bootstrap(app)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

#@app.route('/word_cloud_filtered/<year>/<date>', methods=['POST'])
def word_cloud_filtered(ner_db,years,names,tags):
	try:

		words_freq={}


		new_db = ner_db
		if(len(years)>0):
			new_db = new_db.loc[(new_db['Year'].isin(years))]
		if(len(names)>0):
			new_db = new_db.loc[(new_db['Name'].isin(names))]
		if(len(tags)>0):
			new_db = new_db.loc[(new_db['Tag'].isin(tags))]




		ners  = new_db.NER.unique()


		for ner  in ners:

			words_freq[ner] = new_db.loc[new_db['NER']==ner,'NER'].agg('count')
		words_json = [{'text': str(word), 'weight': int(count)} for word, count in words_freq.items()]

		# now convert it into a string format and return it
		#return json.dumps(words_json)
		return (words_json)
	except Exception as e:
		return '["Error"]'+str(e)

#@app.route('/word_cloud/', methods=['GET'])
def word_cloud(ner_db):
	try:

		words_freq={}



		ners  = ner_db.NER.unique()


		for ner  in ners:

			words_freq[ner] = ner_db.loc[ner_db['NER']==ner,'NER'].agg('count')
		words_json = [{'text': str(word), 'weight': int(count)} for word, count in words_freq.items()]

		# now convert it into a string format and return it
		return words_json
	except Exception as e:
		return '["Error"]'+str(e)


@app.route("/")
def index():
	return render_template('index.html')

@app.route("/explore")
def load_data():
	new_db = sentence_db[['Speech','Name','Component','Year','Date']]


	import re

	with_id=re.sub(' argTable', '" id="argTable', new_db.to_html(index=False,classes ="table table-bordered dataTable argTable"))

	return render_template("explore.html",result = with_id , na_rep="-")

@app.route("/explore/<year>")
def explore(year):
	year = str(year)
	new_db_candidate =sentence_db_candidate[(sentence_db_candidate['Year'].astype(str)== year)]
	new_db = sentence_db[(sentence_db['Year'].astype(str)== year)]
	new_db = new_db[['Speech','Name','Component','Year','Date']]
	dates=[]
	date_items = new_db_candidate.Date.unique()
	for item in date_items:
		date = "<a  class = 'p-4  date-link badge badge-secondary' href ='/chat/"+item+"'>"+ item+"</a>"
		dates.append(date)
	debaters = new_db_candidate.Name.unique()
	debators_html =[]
	for debater in debaters:
		debators_html.append(createChat.CreateImgHtml(debater))

	import re

	with_id=re.sub(' argTable', '" id="argTable', new_db.to_html(index=False,classes ="table table-bordered dataTable argTable"))

	return render_template("explore.html",result = with_id ,dates = dates,debaters = debators_html, na_rep="-")


@app.route("/explore/<year>/<date>")
def explore_date(year,date):
	year = str(year)
	date = str(date)

	new_db = sentence_db[(sentence_db['Year'].astype(str)== year)&(sentence_db['Date'].astype(str)== date)]
	new_db = new_db[['Speech','Name','Component','Year','Date']]

	import re

	with_id=re.sub(' argTable', '" id="argTable', new_db.to_html(index=False,classes ="table table-bordered dataTable argTable"))

	return render_template("explore.html",result = with_id , na_rep="-")


@app.route("/year/<y>")
def year_filter(y):
	y = str(y)
	year_filtered = sentence_db[(sentence_db['Year'].astype(str)== y)]

	return  year_filtered.to_html()
@app.route("/date/<d>")
def date_filter(d):
	d = str(d)
	date_filtered = sentence_db[(sentence_db['Date'].astype(str)== d)]

	return  date_filtered.to_html()

@app.route("/candidate/<c>")
def candidate_filter(c):

	candidate_filtered = sentence_db[(sentence_db['Speaker'].astype(str)== c.lower())]

	return  candidate_filtered.to_html()

@app.route('/ner/', methods=['POST'])
def named_entities_filtered():
    filter_names = request.form.getlist('name')
    filter_years = request.form.getlist('year')
    filter_tags = request.form.getlist('tag')

    data = word_cloud_filtered(ner_db,filter_years,filter_names,filter_tags)


    tags = ner_db.Tag.unique()
    tags.sort()
    names =part_db_candidate.Name.unique()
    names.sort()
    years = ner_db.Year.unique()
    years.sort()
    years = [int(y) for y in years]
    filter_years = [int(y) for y in filter_years]
    return render_template('ner.html',years= years, names =names, tags = tags,filtered_years= filter_years,filtered_names=filter_names,filtered_tags=filter_tags, word_cloud_data=data)

    #return processed_text

@app.route('/ner/', methods=['GET'])
def named_entities():
    #data =""

    #date = "26 Sep 1960"
    #year = "1960"
    data = word_cloud(ner_db)



    tags = ner_db.Tag.unique()
    tags.sort()
    names =part_db_candidate.Name.unique()
    names.sort()
    years = ner_db.Year.unique()
    years.sort()
    years = [str(int(y)) for y in years]

    return render_template('ner.html',years= years, names =names, tags = tags, word_cloud_data=data)


@app.route('/form')
def my_form():
    return render_template('form.html')

@app.route('/chat')
def create_chat():
    return render_template('chat.html')

@app.route('/legalnotice')
def legal_notice():
    return render_template('legalnotice.html')

@app.route('/contact')
def contract_page():
    return render_template('contact.html')

@app.route("/chat/<date>")
def chat_date(date):

	date = str(date)

	new_db = part_db[(part_db['Date'].astype(str)== date)]
	doc=list(new_db['Document'])[0]

	new_ann_db=ann_db[(ann_db['Document'].astype(str)== doc)]
	chat = createChat.createTable(new_db,new_ann_db)


	return render_template("chat.html",chat = chat ,date = date,doc=doc, na_rep="-")

@app.route('/form', methods=['POST'])
def test_data():
    text = request.form['text']

    sentences = sent_tokenize(text)
    final_result = []
    seq =[]
    res =[]
    i =0
    for sentence in sentences:
        res = arg_model.TestModel(sentence.strip(punctuation))

        if(res =="Arg"):
            res = cp_model.TestModel(sentence.strip(punctuation))
            seq = seq_model.TestModel(sentence)

        final_result.append([sentences[i],res,seq])
        i+=1


    return render_template('form.html',text =text, classification_result = final_result)

    #return processed_text







if __name__ == "__main__":

	token_db =  pd.read_csv("data/token_db.csv")
	sentence_db =  pd.read_csv("data/sentence_db.csv")
	part_db =  pd.read_csv("data/part_db.csv")
	token_db_candidate =  pd.read_csv("data/token_db_candidate.csv")
	sentence_db_candidate =  pd.read_csv("data/sentence_db_candidate.csv")
	part_db_candidate =  pd.read_csv("data/part_db_candidate.csv")
	ner_db = pd.read_csv("data/ner_db.csv")
	ann_db = pd.read_csv("data/ann_db.csv")
	cp_model = Model(cp = True)
	try:
		arg_model = Model(cp = False)
		seq_model = Model(cp = False, seq = True)
	except:
		print("arg File not loaded")
	serve(app,  port='8080')
	#app.run(host='127.0.0.1',port ="8080")
