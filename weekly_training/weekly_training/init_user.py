__author__ = 'buyvich'

import os
from sqlalchemy import create_engine

from settings import get_session
from scheme import *
from settings import BASE_DIR

engine = create_engine("sqlite:///%s" % os.path.join(BASE_DIR, 'db.sqlite3'))

user.metadata.create_all(engine)
training.metadata.create_all(engine)

session = get_session()
session.commit()

