from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

STATIC_PATH = os.path.join(BASE_DIR, 'static/')

from mako.lookup import TemplateLookup
TemplateEngine = TemplateLookup(
    directories=[os.path.join(BASE_DIR, 'templates/')],
    output_encoding='utf-8', encoding_errors='replace',
    input_encoding='utf-8')

def get_session():
    engine = create_engine("sqlite:///%s" % os.path.join(BASE_DIR, 'db.sqlite3'))
    Session = sessionmaker(bind=engine)
    return Session()