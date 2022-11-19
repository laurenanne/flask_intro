from flask import Flask, request

app = Flask(__name__)


@app.route('/welcome')
def initial():
    html = "<html><body><h1>welcome</h1></body></html>"
    return html


@app.route('/welcome/home')
def home():
    html = "<html><body><h1>welcome home</h1></body></html>"
    return html


@app.route('/welcome/back')
def back():
    html = "<html><body><h1>welcome back</h1></body></html>"
    return html
