from flask import Flask, render_template, url_for, flash, redirect
from forms import QueryForm


app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'



@app.route("/")
@app.route("/home")
def home():
	return render_template('home.html')


@app.route("/inputform",methods=['GET','POST'])
def inputform():
	form = QueryForm()
	if form.validate_on_submit():
		flash('Query Submitted!','success')
		return redirect(url_for('home'))
	return render_template('inputform.html', form = form)



if __name__ == '__main__':
	app.run(debug=True)