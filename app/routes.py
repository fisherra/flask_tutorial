from app import app
from flask import render_template

@app.route('/')  # decorator modifies function that follows it
@app.route('/index') # use decorator to register function as 'callback'
def index(): # these decorators create an association with url and the index function
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
