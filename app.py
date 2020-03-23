from flask import Flask
from flask import render_template
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
from wtforms import IntegerField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'SuperSecretKey'

class PresForm(FlaskForm):
    num = IntegerField('President Number:', validators=[DataRequired()])
    first_name = StringField('First name:', validators=[DataRequired()])
    last_name = StringField('Last name:', validators=[DataRequired()])
    age = IntegerField('Current Age:', validators=[DataRequired()])
    home_state = StringField('Home state:', validators=[DataRequired()])
    home_city = StringField('Home city:', validators=[DataRequired()])
    terms = IntegerField('Number of terms:', validators=[DataRequired()])
    first_term = IntegerField('Year inaugurated:', validators=[DataRequired()])

    

@app.route('/')
def index():
    return render_template('index.html', pageTitle='America\'s Presidents')

@app.route('/add_pres', methods=['GET', 'POST'])
def add_pres():
    form = PresForm()
    if form.validate_on_submit():
        return "<h2> {0} {1} was President number {2}, from {3}, {4}. They served {5} term(s) starting in {6}, and are currently {7} years old.".format(form.first_name.data, form.last_name.data, form.num.data, form.home_city.data, form.home_state.data, form.terms.data, form.first_term.data, form.age.data)
        
    return render_template('add_pres.html', form=form, pageTitle="Add a new President")


if __name__ == '__main__':
    app.run(debug=True)
