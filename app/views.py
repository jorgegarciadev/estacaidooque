# -*- coding: utf-8 -*-

from flask import render_template
from app import app
from forms import TextInput
from app.users.webtools import validator, pokeSite, answer

@app.route('/', methods = ['GET', 'POST'])
@app.route('/index', methods = ['GET', 'POST'])
def isdownorwhat():
    form = TextInput()
    if form.validate_on_submit():
        form.url.data
        data = answer(form.url.data)
        
        return render_template('isdownorwhat.html', data = data, form = form, title = u"¿Está caido o qué?", value = form.url.data)

    return render_template('isdownorwhat.html', form = form, title = u"¿Está caido o qué?", value = 'github.com')

