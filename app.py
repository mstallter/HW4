from flask import Flask, url_for
from flask import render_template, redirect
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
from wtforms import IntegerField
import secrets
import pymysql
from flask_sqlalchemy import SQLAlchemy
from flask import request
from sqlalchemy import or_
#import os

#dbhost = os.environ.get('DBHOST')
#dbuser = os.environ.get('DBUSER')
#dbpass = os.environ.get('DBPASS')
#dbname = os.environ.get('DBNAME')

conn = "mysql+pymysql://{0}:{1}@{2}/{3}".format(secrets.dbuser, secrets.dbpass, secrets.dbhost, secrets.dbname)
#conn = "mysql+pymysql://{0}:{1}@{2}/{3}".format(dbuser, dbpass, dbhost, dbname)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'SuperSecretKey'
app.config['SQLALCHEMY_DATABASE_URI'] = conn
db = SQLAlchemy(app)

class mstallter_presidents(db.Model):
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
    all_pres = mstallter_presidents.query.all()
    return render_template('index.html', pres = all_pres, pageTitle='America\'s Presidents')

@app.route('/add_pres', methods=['GET', 'POST'])
def add_pres():
    form = PresForm()
    if form.validate_on_submit():
        Pres = mstallter_presidents(NUM = form.num.data, FIRSTNAME = form.first_name.data, LASTNAME=form.last_name.data, AGE=form.age.data, HOMESTATE=form.home_state.data, HOMECITY=form.home_city.data, TERMS=form.terms.data, YROFFRSTTERM=form.first_term.data)
        db.session.add(Pres)
        db.session.commit()
        return redirect('/')
    return render_template('add_pres.html', form=form, pageTitle="Add a new President")

@app.route('/delete_pres/<int:Num>', methods=['GET', 'POST'])
def delete_pres(Num):
    if request.method == 'POST':
        pres = mstallter_presidents.query.get_or_404(Num)
        db.session.delete(pres)
        db.session.commit()
        return redirect('/')
    else:     
        return redirect('/')

@app.route('/pres/<int:Num>', methods=['GET','POST'])
def get_pres(Num):
    pres = mstallter_presidents.query.get_or_404(Num)
    return render_template('pres.html', form=pres, pageTitle='President Details', legend="Update an Entry")

@app.route('/pres/<int:Num>/update', methods=['GET','POST'])
def update_pres(Num):
    pres = mstallter_presidents.query.get_or_404(Num)
    form = PresForm()
    if form.validate_on_submit():
        pres.NUM = form.num.data
        pres.FIRSTNAME = form.first_name.data
        pres.LASTNAME = form.last_name.data
        pres.AGE = form.age.data
        pres.HOMESTATE = form.home_state.data
        pres.HOMECITY = form.home_city.data
        pres.TERMS = form.terms.data
        pres.YROFFRSTTERM = form.first_term.data
        db.session.commit()
        return redirect(url_for('get_pres', Num=pres.NUM))
    form.num.data = pres.NUM
    form.first_name.data = pres.FIRSTNAME
    form.last_name.data = pres.LASTNAME
    form.age.data = pres.AGE
    form.home_state.data = pres.HOMESTATE
    form.home_city.data= pres.HOMECITY
    form.terms.data = pres.TERMS
    form.first_term.data = pres.YROFFRSTTERM
    return render_template('update_pres.html', form=form, pageTitle = 'Update President', legend="Update an Entry")

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method=='POST':
        form = request.form
        search_value = form["search_string"]
        search = "%{0}%".format(search_value)
        results = mstallter_presidents.query.filter(or_(mstallter_presidents.FIRSTNAME.like(search),
        mstallter_presidents.LASTNAME.like(search))).all()
        return render_template('index.html', pres=results, pageTitle='Search President', legend='Search Results')
    else:
        return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
