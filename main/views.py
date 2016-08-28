from flask import Flask, render_template, request, redirect, jsonify, session, url_for
from . import main
import sys

sys.path.append("..")
from model import User

@main.route('/', methods=['GET', 'HEAD'])
def index():
    if request.method == 'GET':
        return render_template('index.html')

@main.route('/login', methods=['POST'])
def login():
    print "123"
    username = request.form['username']
    password = request.form['password']
    user = User.query.filter_by(username=username).first()
    if user != None and user.verify_password(password):
        auth = True
        session['username'] = username
    else:
        auth = False
    cookie = request.form['remember_me'] == 'true'
    print session
    return jsonify(auth = auth, isCookie = cookie)

@main.route('/a123')
def a123():
    print session
    if 'username' in session:
        return '123'
    else:
        return redirect(url_for('main.index'))

@main.app_errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
