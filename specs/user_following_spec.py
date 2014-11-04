from co import factory, errors

from expects import expect, be_true, contain, raise_error

with description('Follow user'):
    with before.each:
        self.nickname = '@foolano'
        self.other_nickname = '@da_kewl_guru'
        self.service = factory.create_users_service()

    with it('returns all users followed by a user'):
        self.service.register(self.nickname)
        self.service.register(self.other_nickname)

        self.service.follow_to(self.nickname, self.other_nickname)

        expect(self.service.follows_to(self.nickname)).to(contain(self.other_nickname))

    with context('when user is not registered'):
        with it('raises an error'):
            self.service.register(self.other_nickname)

            expect(lambda: self.service.follow_to(self.nickname, self.other_nickname)).to(raise_error(errors.UserDoesNotExistError))

    with context('when target user is not registered'):
        with it('raises an error'):
            self.service.register(self.nickname)

            expect(lambda: self.service.follow_to(self.nickname, self.other_nickname)).to(raise_error(errors.UserDoesNotExistError))
