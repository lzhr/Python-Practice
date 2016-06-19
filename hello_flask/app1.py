from flask import Flask,render_template,redirect
from flask.ext.bootstrap import Bootstrap
from flask.ext.script import Server,Manager
from flask.ext.moment import Moment
from datetime import datetime


app = Flask(__name__)
manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)

@app.route('/')
def index():
    return render_template('index.html',current_time=datetime.utcnow())

@app.route('/user/<name>')
def user(name):
    if name == 'lzhr':
      return redirect('http://github.com/lzhr')
    return render_template('user.html',name=name)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404

server=Server(use_debugger=True)

if __name__ == "__main__":
    manager.run()
