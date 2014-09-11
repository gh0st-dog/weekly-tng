__author__ = 'buyvich'

from pprint import pprint
import logging

from tornado.web import RequestHandler

from weekly_training.settings import TemplateEngine, get_session
from weekly_training.models import *


LOG = logging.getLogger()

class BaseHandler(RequestHandler):

    def initialize(self):
        self.session = get_session()

class IndexHandler(BaseHandler):

    def get(self):
        template = TemplateEngine.get_template('index.html')
        self.write(template.render_unicode(xsrf=self.xsrf_token))


class TrainingHandler(BaseHandler):

    def get(self):

        trainings = self.session.query(Training).all()
        pprint(trainings)
        self.write('OK')

    def post(self):
        user = self.session.query(User).first()
        pprint(self.request.body_arguments)
        name = self.get_argument('name')
        goal = self.get_argument('goal')
        tng = Training(name=name, goal=goal, user=user)
        self.session.add(tng)
        self.session.commit()
        self.write('OK')