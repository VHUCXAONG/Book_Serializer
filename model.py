# -*- coding: utf-8 -*-
from run import db
from werkzeug.security import generate_password_hash, check_password_hash

class Book(db.Model):
    __tablename__ = 'book'
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.UnicodeText(128), index=True)
    chapter_number = db.Column(db.Integer)
    source_url = db.Column(db.String(128))
    page_url_rule = db.Column(db.String(128))
    content_url_rule = db.Column(db.String(128))
    username = db.Column(db.String(64), index=True)
    def __init__(self, name, chapter, url, username, page_url_rule, content_url_rule):
        self.book_name = name
        self.chapter_number = chapter
        self.source_url = url
        self.username = username
        self.page_url_rule = page_url_rule
        self.content_url_rule = content_url_rule

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128), index=True)
    book_list = db.Column(db.UnicodeText(1000), index=True)

    def __init__(self, username, book_list):
        self.username = username
        self.book_list = book_list

    @property
    def password(self):
        raise AttributeError('password is not reaadable')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)
