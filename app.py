# pip install flask
from flask import Flask, render_template, request, redirect, url_for
from model import add_user

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        password_check = request.form['password_check']
        add_user(name, email, password)
        return redirect('/users/'+ name)
    return render_template('index.html')
    #  jsonify {"data":['apple, banana']} - возврат в формате json

@app.route('/users/<name>')
def user_page(name):
    return render_template('user.html', name=name)

    # f'''<h1>Title</h1>
    # <p>Hello, {name.title()}!</p>
    # <p>What did you eat for breakfast?</p>'''
# @app.route('/users/daniil')
# def user_daniil():
#     return 'Hello, Daniil!'

# @app.route('/users/milena')
# def user_milena():
#     return 'Hello, Milena!'

app.run(debug=True)