from co import factory, errors

from expects import expect, contain, raise_error

with description('Publish a co for a user'):

    with before.each:
        self.nickname = '@foolano'
        self.co = 'que pasa co?'
        self.service = factory.create_users_service()

    with it('publishes a co'):
        self.service.register(self.nickname)

        self.service.publish_co(self.nickname, self.co)

        expect(self.service.cos_for(self.nickname)).to(contain(self.co))

    with context('when user is not registered'):
        with it('raises an error'):
            expect(lambda: self.service.publish_co(self.nickname, self.co)).to(raise_error(errors.UserDoesNotExistError))


