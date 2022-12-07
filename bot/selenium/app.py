from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/login', methods=['post'])
def login():
    if request.form.get('username') == 'admin' and request.form.get('password') == 'secret':
        return "Ok"
    return "Nope"


@app.route('/')
def home():
    return render_template("home.html")


app.run()
