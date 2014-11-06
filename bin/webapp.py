import httplib
import json

import tornado.ioloop
import tornado.web
import tornado.options

from co import factory, errors

class UsersHandler(tornado.web.RequestHandler):

    def initialize(self, users_service):
        self.users_service = users_service

    def post(self):
        try:
            nickname = json.loads(self.request.body)['nickname']
            self.users_service.register(nickname)
            self.set_status(httplib.CREATED)
        except errors.UserAlreadyRegisteredError:
            self.write({'error': 'Nickname already taken'})
            self.set_status(httplib.CONFLICT)


class FollowingsHandler(tornado.web.RequestHandler):

    def initialize(self, users_service):
        self.users_service = users_service

    def get(self, nickname):
        try:
            following = users_service.follows_to(nickname)
            self.write({'result': following})
        except errors.UserDoesNotExistError:
            self.write({'error': 'User does not exist'})
            self.set_status(httplib.NOT_FOUND)

    def post(self, nickname):
        try:
            target = json.loads(self.request.body)['nickname']
            users_service.follow_to(nickname, target)
            self.set_status(httplib.CREATED)
        except errors.UserDoesNotExistError:
            self.write({'error': 'User does not exist'})
            self.set_status(httplib.NOT_FOUND)


class CosHandler(tornado.web.RequestHandler):

    def initialize(self, users_service):
        self.users_service = users_service

    def get(self, nickname):
        try:
            cos = users_service.cos_for(nickname)
            self.write({'result': cos})
        except errors.UserDoesNotExistError:
            self.write({'error': 'User does not exist'})
            self.set_status(httplib.NOT_FOUND)

    def post(self, nickname):
        try:
            co = json.loads(self.request.body)['co']
            users_service.publish_co(nickname, co)
            self.set_status(httplib.CREATED)
        except errors.UserDoesNotExistError:
            self.write({'error': 'User does not exist'})
            self.set_status(httplib.NOT_FOUND)


users_service = factory.create_durable_users_service()
application = tornado.web.Application([
    (r'/users', UsersHandler, dict(users_service=users_service)),
    (r'/users/(?P<nickname>[^/]*)/following', FollowingsHandler, dict(users_service=users_service)),
    (r'/users/(?P<nickname>[^/]*)/cos', CosHandler, dict(users_service=users_service)),
], debug=True)

if __name__ == '__main__':
    tornado.options.parse_command_line()
    application.listen(5000)
    tornado.ioloop.IOLoop.instance().start()
