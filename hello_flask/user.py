
from flask import Flask,render_template,abort,redirect

app = Flask(__name__)

@app.route('/user/<name>')
def sayHello(name):
    if name == 'baidu':
        return redirect('http://www.baidu.com')
    elif name == 'NO':
        return abort(404)

    return render_template('user.html',user=name)

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug = True)
