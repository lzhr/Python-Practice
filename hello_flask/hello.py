from flask import Flask,render_template,abort,redirect

app = Flask(__name__)

@app.route('/')
def index():
    return redirect('/hello/guest')

#@app.route('/hello')
#def hello_world():
#    return 'Hello World!'
@app.route('/hello/<name>')
def hello_world(name):
    return 'Hello World!<br> %s' % name

if __name__ == '__main__':
    #app.run(host='0.0.0.0',debug = True)
    app.run(debug = True)
