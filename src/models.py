import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False, unique=True)
    name = Column(String(50), nullable=False)
    lastname = Column(String(100), nullable=False)
    email = Column(String(30), unique=True)
    comments = relationship("Comment", back_populates="person")
    posts = relationship("Post", back_populates="person")

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    person_id = Column(Integer, ForeignKey('user.id'))
    person = relationship("User", back_populates="posts")
    comments = relationship("Comment", back_populates="posts")


class Comment(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(150), nullable=False)
    person_id = Column(Integer, ForeignKey('user.id'))
    post_id = Column(Integer, ForeignKey('post.id'))
    person = relationship("User", back_populates="comments")
    posts = relationship("Post", back_populates="comments")

class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    url = Column(String(300), nullable=False)
    post_id = Column(Integer, ForeignKey('post.id'))

class Follower(Base):
    __tablename__ = 'follower'
    id = Column(Integer, primary_key=True)
    user_from_id = Column(Integer, ForeignKey('user.id'))
    user_to_id = Column(Integer, ForeignKey('user.id'))


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e