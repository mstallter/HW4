from flask import Flask
from flask import render_template
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
from wtforms import IntegerField
import secrets
import pymysql
from flask_sqlalchemy import SQLAlchemy

conn = "mysql+pymysql://{0}:{1}@{2}/{3}".format(secrets.dbuser, secrets.dbpass, secrets.dbhost, secrets.dbname)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'SuperSecretKey'
app.config['SQLALCHEMY_DATABASE_URI'] = conn
db = SQLAlchemy(app)

class mstallter_Pres(db.Model):
    NUM = db.Column(db.Integer, primary_key = True)
    FIRSTNAME = db.Column(db.String(225))
    LASTNAME = db.Column(db.String(225))
    AGE = db.Column(db.Integer)
    HOMESTATE = db.Column(db.String(225))
    HOMECITY = db.Column(db.String(225))
    TERMS = db.Column(db.Integer)
    YROFFRSTTERM = db.Column(db.Integer)

    def __repr__(self):
        return "id: {0} | Num: {1} | First Name: {2} | Last Name: {3} | Age: {4} | Home State: {5} | Home City: {6} |\
            Terms: {7} | Year of First Term: {8}".format(self.NUM, self.FIRSTNAME, self.LASTNAME, self.AGE, self.HOMESTATE, \
            self.HOMECITY, self.TERMS, self.YROFFRSTTERM)

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
    all_pres = mstallter_Pres.query.all()
    return render_template('index.html', pres = all_pres, pageTitle='America\'s Presidents')

@app.route('/add_pres', methods=['GET', 'POST'])
def add_pres():
    form = PresForm()
    if form.validate_on_submit():
        Pres = mstallter_Pres(NUM = form.num.data, FIRSTNAME = form.first_name.data, LASTNAME=form.last_name.data, \
            AGE=form.age.data, HOMESTATE=form.home_state.data, HOMECITY=form.home_city.data, TERMS=form.terms.data, YROFFRSTTERM=form.first_term.data)
        db.session.add(Pres)
        db.session.commit()
        return "<h2> {0} {1} was President number {2} and was from {3}, {4}. They served {5} terms starting in {6} are currently {7} years old.".format(\
            form.first_name.data,form.last_name.data,form.num.data,form.home_city.data,form.home_state.data,form.terms.data,form.first_term.data,form.age.data)
    return render_template('add_pres.html', form=form, pageTitle="Add a new President")


if __name__ == '__main__':
    app.run(debug=True)
