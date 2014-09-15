__author__ = 'buyvich'

import os
from sqlalchemy import create_engine

from settings import get_session
from models import User
from scheme import *

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

engine = create_engine("sqlite:///%s" % os.path.join(BASE_DIR, 'db.sqlite3'))

user.metadata.create_all(engine)
training.metadata.create_all(engine)

session = get_session()
user = User(name='admin', password='123123')
session.add(user)
session.commit()

