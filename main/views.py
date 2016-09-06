# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, redirect, jsonify, session, url_for
from . import main
import sys

sys.path.append("..")
from model import User, Book

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/login', methods=['POST'])
def login():
    print "login"
    print ""
    username = request.form['username']
    password = request.form['password']
    user = User.query.filter_by(username=username).first()
    if user != None and user.verify_password(password):
        auth = True
        session['username'] = username
    else:
        auth = False
    cookie = request.form['remember_me'] == 'true'
    print "session:"
    print session
    print ""
    return jsonify(auth = auth, isCookie = cookie)

@main.route('/book')
def main1():
    print session
    if 'username' in session:
        return render_template('main.html')
    else:
        return redirect(url_for('main.index'))

@main.route('/loadbook', methods=['POST'])
def loadbook():
    print "book"
    print ""
    username = session['username']
    user = User.query.filter_by(username=username).first()
    data = dict()
    data['book_name'] = eval(user.book_list)
    data['book_chapter'] = [None] * len(data['book_name'])
    data['book_source'] = [None] * len(data['book_name'])
    for i, (name) in enumerate(data['book_name']):
        book = Book.query.filter_by(book_name=name).first()
        data['book_chapter'][i] = book.chapter_number
        data['book_source'][i] = book.source
    print "data:"
    print data
    print ""
    return jsonify(book_name=data['book_name'], book_chapter=data['book_chapter'], book_source=data['book_source'])


@main.app_errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
