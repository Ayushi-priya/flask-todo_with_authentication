from flask_login import UserMixin
from datetime import datetime
from . import db

class User(UserMixin, db.Model):
    # __tablename__='user'

    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    name = db.Column(db.String(1000), nullable=False)
    password = db.Column(db.String(250), nullable=False)
    
class Todo(db.Model):
    # __tablename__='todo'
    # sno=db.Column(db.Integer,primary_key=True)
    # user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    # user = db.relationship("User", backref=db.backref("user", uselist=False))

    sno=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(200),nullable=False)
    desc=db.Column(db.String(200),nullable=False)
    date_created=db.Column(db.DateTime,default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.title}"