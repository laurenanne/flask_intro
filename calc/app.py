# Put your app in here.
from flask import Flask, request
from operations import *

app = Flask(__name__)


@app.route('/add')
def addMethod():
    a = int(request.args["a"])
    b = int(request.args["b"])
    return str(add(a, b))


@app.route('/sub')
def subMethod():
    a = int(request.args["a"])
    b = int(request.args["b"])
    return str(sub(a, b))


@app.route('/mult')
def multMethod():
    a = int(request.args["a"])
    b = int(request.args["b"])
    return str(mult(a, b))


@app.route('/div')
def divMethod():
    a = int(request.args["a"])
    b = int(request.args["b"])
    return str(div(a, b))


@app.route('/math/<operation>')
def formulas(operation):
    a = int(request.args["a"])
    b = int(request.args["b"])
    dict_operators = {"add": add(a, b), "sub": sub(
        a, b), "mult": mult(a, b), "div": div(a, b)}
    return str(dict_operators[operation])
