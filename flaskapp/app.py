# Flask Imports
from flask import Flask, render_template, url_for, flash, redirect, request, session 
from forms import QueryForm
from flask_sqlalchemy import SQLAlchemy

# Framework Imports
import pandas as pd
import numpy as np

from nltk.cluster import KMeansClusterer
import nltk  

from sklearn import cluster
from sklearn import metrics

from utils import *


app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
# db = SQLAlchemy(app)


# class User(db.Model):
# 	id = db.Column(db.Integer, primary_key = True)
# 	username = db.Column(db.String(20), unique=True, nullable=Flase)
# 	posts = db.relationship('Post', backref='')

# 	def __repr__(self):
# 		return f"User('{self.username}')"

# class Book(db.Model):
# 	id = db.Column(db.Integer, primary_key = True)
# 	title = db.Column(db.String(100), unique=True, nullable=Flase)



@app.route("/")
@app.route("/home")
def home():
	return render_template('home.html')


# @app.route("/inputform",methods=['GET','POST'])
# def inputform():
# 	form = QueryForm()
# 	if form.validate_on_submit():
# 		flash('Query Submitted!','success')
# 		return redirect(url_for('home'))
# 	return render_template('inputform.html', form = form)


@app.route("/inputform",methods=['GET','POST'])
def inputform():
	form = QueryForm()
	if form.validate_on_submit():

		query = form.query.data
		df = pd.read_pickle('cmu_data_phrase.pkl')

		#Get top-n entries by score ranking
		df['score'] = df.apply(lambda row: get_score(query, row.noun_phrase, row.sentiment, alpha=0.95), axis = 1) 
		df_topn = df.nlargest(500, 'score')
		df_topn.reset_index(inplace=True)


		recommendations = get_recommendation(query, df, df_topn, n=500, NUM_CLUSTERS=10)
		# session['btitle'] = []
		# for book in recommendations:
		# 	session['btitle'].append(book['book_title'])

		# flash('Query Submitted!','success')
		return render_template('output.html', recommendations = recommendations, query=query)
	return render_template('inputform.html', form = form)

@app.route("/feedback",methods=['GET','POST'])
def feedback():
	if request.method == 'POST':
		username = request.form['username']
		yes = 0
		no = 0
		for i in range(1,31):
			if(request.form.get("feed{}".format(i))) == "Y":
				yes = yes + 1
			elif(request.form.get("feed{}".format(i))) == "N":
				no = no +1
		# no = 30 - yes
		return render_template('success.html', username=username, yes=yes, no=no)







if __name__ == '__main__':
	app.run(debug=True)