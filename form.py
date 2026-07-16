from flask import Flask, render_template, url_for, redirect, session
from flask_wtf import FlaskForm
from wtforms import ValidationError, StringField,DateField,SubmitField,HiddenField
from wtforms.validators import DataRequired

class RegistrationForm(FlaskForm):
    id =HiddenField()
    name = StringField('イベント名', validators=[DataRequired()])
    date = DateField('日付:', format='%Y-%m-%d')
    submit = SubmitField()