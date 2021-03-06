from pybo import db

class Diary(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    user = db.relationship('User', backref=db.backref('diary_set'))

class MusicRec(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    diary_id = db.Column(db.Integer, db.ForeignKey('diary.id', ondelete='CASCADE'))
    diary = db.relationship('Diary', backref=db.backref('musicrec_set'))
    musicname = db.Column(db.Text(), nullable=False)
    singer = db.Column(db.Text(), nullable=True)
    lyrics = db.Column(db.Text(), nullable=True)
    genre = db.Column(db.Text(), nullable=True)
    grade = db.Column(db.Integer(), nullable=True)
    create_date = db.Column(db.DateTime(), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    user = db.relationship('User', backref=db.backref('musicrec_set'))

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
