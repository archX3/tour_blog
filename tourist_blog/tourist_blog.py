import sys, os
sys.path.append(os.getcwd())

from flask import Flask, render_template, redirect, session, request, url_for

app = Flask(__name__)


@app.route('/')
def hello_world() :
    return 'Hello World!'


if __name__ == '__main__' :
    app.run()
