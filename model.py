from . import db

class Book(db.Model):
    __tablename__ = 'book'
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(64), unique=True, index=True)
    chapter_number = db.Column(db.Integer)
    source = db.Column(db.String(64))

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password = db.Column(db.String(64), index=True)
    book_list = db.Column(db.String(1000), index=True)
