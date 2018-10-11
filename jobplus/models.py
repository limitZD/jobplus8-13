from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin

db = SQLAlchemy()


class Base(db.Model):
	__abstract__ = True
	created_at = db.Column(db.DataTime,default=datetime.utcnow)
	updated_at = db.Column(db.DataTime,default=datetime.utcnow,onupdate=datetime.utcnow)

class User(Base,UserMixin):
	__tablename__ = 'user'

	id = db.Column(db.Integer,primary_key=True)
	username = db.Column(db.String(32),unique=True, nullable=False)
	email = db.Column(db.String(64),unique=True,index=True,nullable=False)
	_password = db.Column('password',db.String(256),nullable=False)
	sex = db.Column(db.String(32),)
	age = db.Column(db.Integer(32))
	work_age = db.Column(db.Integer(32))
	phone = db.Column(db.Integer)
	degree = db.Column(db.String(32))

	position_id = db.relationship('Position',order_by='position_id',backref='user')
	company_id	= db.relationship('Company',order_by='company_id',backref='user')

class Position(Base):
	__tablename__ = 'position'

	id = db.Column(db.Integer,primary_key=True)
	position_id = db.relationship('User',backref=backref('position_id'),order_by=id)
	position_name = db.Column(db.String(128),unique=True, nullable=False)

class Company(Base):
	__tablename__ = 'company'

	id = db.Column(db.Integer,primary_key=True)
	company_id = db.relationship('User',backref=backref('company_id'),order_by=id)

	company_type = db.Column(db.String(64))
	city = db.Column(db.String(32))
	financing = db.Column(db.String(32))
	intro = db.Column(db.String(128), default='GongSi JiShao')

