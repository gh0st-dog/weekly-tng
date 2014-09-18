__author__ = 'buyvich'

from pprint import pprint
import logging
import functools
import json


import sqlalchemy
from tornado.web import RequestHandler

from weekly_training.settings import TemplateEngine, get_session
from weekly_training.models import *


LOG = logging.getLogger()


def auth(f):
    @functools.wraps(f)
    def wrapper(s, *args, **kwargs):
        '''
        @type s: RequestHandler
        '''

        user = s.get_secure_cookie('user')
        if not user:
            s.redirect('/login/')
        return f(s, *args, **kwargs)
    return wrapper


class BaseHandler(RequestHandler):

    def initialize(self):
        self.session = get_session()

    def get_current_user(self):
        user = self.get_secure_cookie('user')
        if user:
            return self.session.query(User).filter(
                User.login == user).one()
        return None


class IndexHandler(BaseHandler):

    @auth
    def get(self):
        template = TemplateEngine.get_template('index.html')
        self.write(template.render_unicode(xsrf=self.xsrf_token,
                                           user=self.get_current_user()))


class TrainingHandler(BaseHandler):

    @auth
    def get(self):
        pprint(self.request)
        #callback = self.get_argument('callback')
        user = self.get_current_user()
        trainings = self.session.query(Training).filter(
            Training.user == user
        ).all()
        result = []
        for training in trainings:
            result.append(training.to_dict())
        self.set_header('Content-Type', 'application/json')
        pprint(result)
        self.write(json.dumps(result))

    @auth
    def post(self):
        user = self.get_current_user()
        pprint(self.request.body_arguments)
        pprint(self.request.body)
        data = json.loads(self.request.body)
        tng = Training(name=data['name'], goal=data['goal'],
                       user=user, units=data['units'])
        self.session.add(tng)
        self.session.commit()
        self.write('OK')


class LoginHandler(BaseHandler):

    def get(self):
        template = TemplateEngine.get_template('login.html')
        self.write(template.render_unicode(xsrf=self.xsrf_token))

    def post(self):
        login = self.get_argument('username')
        password = self.get_argument('password')
        try:
            self.session.query(User).filter(
                User.login == login,
                User.password == password).one()
        except sqlalchemy.orm.exc.NoResultFound:
            self.redirect('/login/')
        self.set_secure_cookie('user', login)
        self.redirect('/')


class LogoutHandler(BaseHandler):

    def get(self):
        self.clear_cookie('user')
        self.redirect('/')