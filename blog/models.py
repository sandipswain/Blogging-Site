from blog import db,login_manager
from datetime import datetime
from flask_login import UserMixin
#UserMixin provides various attributes like is_autheicated,is_active,is_anonynomous

#A function to get an user by an ID
@login_manager.user_loader
def load_user(user_id):
    #Returning the user for that ID
    return User.query.get(int(user_id))

#Inheriting from a class UserMixin and db.Model
class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False,
                           default='profile.jpg')
    password = db.Column(db.String(60), nullable=False)
    # bacref is similar to adding a column in Post Model
    # lazy argument defines the data when SQLALCHEMY loads the data from the database
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f'User("{self.username}","{self.email}","{self.image_file}")'


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False,
                            default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f'Post("{self.title}","{self.date_posted}")'
