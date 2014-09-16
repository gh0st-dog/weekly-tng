__author__ = 'buyvich'

import os

from tornado import options
from tornado.ioloop import IOLoop
from tornado.web import StaticFileHandler, Application, url
from tornado.httpserver import HTTPServer

from weekly_training.settings import BASE_DIR, STATIC_PATH
import handlers

def make_app():
    return Application(
        [url(r'/', handlers.IndexHandler),
         url(r'/training/', handlers.TrainingHandler),
         url(r'/login/', handlers.LoginHandler),
         url(r'/logout/', handlers.LogoutHandler),
         ],
        debug=True,
        static_path=STATIC_PATH,
        cookie_secret='5f23aa988ab6c68206377cd6ee1edcee921b2365',
    )


def main():
    options.parse_command_line()
    app = make_app()
    app.listen(8080)
    IOLoop.instance().start()

if __name__ == '__main__':
    print 'Start server at 8080'
    print 'Press Ctrl+C for stop'
    main()
