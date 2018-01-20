import sys, os
sys.path.append(os.getcwd())

from tourmodel import Users
from flask import Flask, render_template, redirect, session, request, url_for
import flask_login

app = Flask(__name__)

# @app.before_first_request
# #this is to create the table if it has not been created already
# def initialize_tables():
#     connect_db()
#     if not user.table_exists():
#         user.create_table()
#     disconnect_db()
#
# @app.before_request
# #this connects to the table before A request is made
# def connect_db():
#     DBSingelton.getInstance().connect()
#
# @app.teardown_request
# #this close down the table.
# def disconnect_db(err=None):
#     DBSingelton.getInstance().close()


#
# @app.route('/')
# def hello_world() :
#     return 'Hello World!'



@app.route('/login',methods=['GET','POST'])
def login():
    if request.form.get('username') == Users.username and request.form.get('password') == Users.password:
        return render_template('login.html')




if __name__ == '__main__' :
    app.run()
