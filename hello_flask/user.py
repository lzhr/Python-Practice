from flask import Flask,render_template,abort,redirect

app = Flask(__name__)

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
