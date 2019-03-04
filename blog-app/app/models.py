from . import db
from . import login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    pass_secure = db.Column(db.String(255))
    blogs = db.relationship('Blog',backref = 'user',lazy="dynamic")
    comments = db.relationship('Comment',backref = 'user',lazy="dynamic")
   

   
    @property
    def password(self):
            raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
            self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
            return check_password_hash(self.pass_secure,password)

    def __repr__(self):
        return f'User {self.username}'

class Blog(db.Model):
    __tablename__ = 'blogs'
    id = db.Column(db.Integer,primary_key = True)
    blog = db.Column(db.String(500))
    posted = db.Column(db.DateTime,default=datetime.utcnow)
    comments = db.relationship('Comment',backref = 'blog',lazy="dynamic")
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    
    def save_blogs(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_blogs(cls):
        blogs = Blog.query.all()
        return blogs   

    def __repr__(self):
        return f'User {self.blog}'

class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer,primary_key = True)
    comment= db.Column(db.String(500))
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    blog_id = db.Column(db.Integer,db.ForeignKey('blogs.id'))

    def save_comments(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f'User {self.comment}'

class Subscriber(UserMixin, db.Model):
   __tablename__="subscribers"

   id = db.Column(db.Integer, primary_key=True)
   name = db.Column(db.String(255))
   email = db.Column(db.String(255),unique = True,index = True)


   def save_subscriber(self):
       db.session.add(self)
       db.session.commit()       

# class Quote:
#     def __init__(self,id,author,quote):
#         self.id =id
#         self.author = author
#         self. quote = quote
    