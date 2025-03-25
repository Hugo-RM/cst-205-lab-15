# run with: flask --app hello_flask --debug run 

from flask import Flask, render_template
from flask_bootstrap import Bootstrap5

app = Flask(__name__)

@app.route('/')
def hello():
    s1 = 'Hello world from Flask!'
    s2 = '<p>Fake person cause my friends didn\'t respond: LMAO</p>'
    return s1 + s2

@app.route('/hugo')
def t_test():
    return render_template('template.html')

bootstrap = Bootstrap5(app)