from flask import render_template, flash, redirect
from app import app
from app.forms import LoginForm


@app.route('/')  # decorator modifies function that follows it
@app.route('/index')  # use decorator to register function as 'callback'
def index():  # these decorators create an association with url and the index function
    user = {'username': 'Fisher'}
    posts = [
        {
            'author': {'username': 'Jack'},
            'body': 'Beautiful day in Denver!'
        },
        {
            'author': {'username': 'Sam'},
            'body': "That's not social distancing!"
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)
