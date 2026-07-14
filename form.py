from flask import Flask, render_template, url_for, redirect, session
from flask_wtf import FlaskForm
from wtforms import ValidationError, StringField,DateField,SubmitField
from wtforms.validators import DataRequired

class RegistrationForm(FlaskForm):
    name = StringField('ユーザー名', validators=[DataRequired()])
    date = DateField('日付を記入してください:', format='%Y-%m-%d')
    submit = SubmitField()