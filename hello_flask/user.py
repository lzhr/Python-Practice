from flask import Flask,render_template,abort,redirect
from flask.ext.bootstrap import Bootstrap
from flask.ext.moment import Moment

app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)

@app.route('/user/<name>')
def user(name):
    #if name == 'baidu':
    #    return redirect('http://www.baidu.com')
    #elif name == 'NO':
    #    return abort(404)
    return render_template('user.html',user=name)

@app.route('/page')
def page():
    return render_template('page.html')

if __name__ == '__main__':
    #app.run(host='0.0.0.0',debug = True)
     app.run(debug=True)
