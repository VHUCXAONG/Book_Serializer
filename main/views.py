from flask import Flask, render_template, request
from . import main

@main.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    if request.method == 'POST':
        return '123'

@main.route('/login', methods=['POST'])
def login():
    print request.form['username']
    return '<h1>success</h1>'


@main.app_errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
