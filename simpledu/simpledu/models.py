from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(32))
    publish_courses = db.relationship('Course')
    created_time = db.Column(db.DateTime, default=datetime.utcnow)
    updated_time = db.Column(db.DateTime,default = datetime.utcnow,onupdate = datetime.utcnow)

class Course(db.Model):
    __tablename__ = 'Course'
    
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(128),unique = True,nullable=False)
    author_id = db.Column(db.Integer,db.ForeignKey('user.id',ondelete='CASCADE'))
    author = db.relationship('User',uselist=False)
    created_time = db.Column(db.DateTime, default=datetime.utcnow)
    updated_time = db.Column(db.DateTime,default = datetime.utcnow,onupdate = datetime.utcnow)
