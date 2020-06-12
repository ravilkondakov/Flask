# -*- coding: utf-8 -*
from flask import render_template, flash, redirect, url_for
from cat import app
from cat.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    user = {'username': ', меня зовут Равиль Кондаков'}
    posts = [
        {
            'author': {'username': 'София Катеринина'},
            'body': 'Я тебя люблю'
        }, {'author': {'username': 'Дмитрий Семеняка'},
            'body': 'слышь, я тут зп получил! купил себе 16 пачек табак!!! Я уже сру им! КАРЛ!'},
        {'author': {'username': 'Дмитрий Смирнов'},
         'body': 'Хватит уже учить свой Flask!!!'}
    ]
    return render_template('index.html', title='poet',
                           user=user, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'login requested for user {form.username.data}, remember_me ={form.remember_me.data}')
        return redirect(url_for('index'))

    return render_template('login.html', title='Войти', form=form)
