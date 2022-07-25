from random import choices
from flask import Flask, render_template, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import (StringField,SubmitField, BooleanField, DateTimeField,RadioField,SelectField,TextField,TextAreaField)
from wtforms.validators import DataRequired
app = Flask (__name__)
app.config['SECRET_KEY'] = 'anothersecretkey'

class InformationForm(FlaskForm):
    user_name = StringField(validators = [DataRequired()])
    password = StringField(validators = [DataRequired()])
    submit = SubmitField('Submit')

@app.route('/', methods = ['GET','POST'])
def index():
    form = InfoForm()
    if form.validate_on_submit():
        session['user_name'] = form.user_name.data
        session['password'] = form.password.data
        return redirect(url_for('report'))
    return render_template('index.html', form = form)

@app.route('/report')
def report():
    return render_template('report.html')

if __name__ == '__main__':
    app.run(debug=True)