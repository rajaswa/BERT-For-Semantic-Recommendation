from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class QueryForm(FlaskForm):
	query = StringField('Query', validators = [DataRequired(), Length(min=3)])
	submit = SubmitField('Submit Query')
