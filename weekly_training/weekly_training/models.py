# coding: utf-8
__author__ = 'buyvich'

import json

import sqlalchemy.orm as orm
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

from scheme import *

Base = declarative_base()

class BaseModel(Base):
    __abstract__ = True

    def to_dict(self):
        result = {}
        for key in self.__mapper__.c.keys():
            result[key] = getattr(self, key)
        return result

    def to_json(self):
        return json.dumps(self.to_dict())

    @property
    def session(self):
        return orm.session.object_session(self)



class User(BaseModel):
    __table__ = user

    def __repr__(self):
        return '<User login=%s>' % (
            self.login)


class Training(BaseModel):

    __table__ = training

    user = orm.relation(User, backref='trainings')

    def __repr__(self):
        return '<Training name=%s, type=%s, goal=%s>' % (
            self.name, self.tng_type, self.goal)
