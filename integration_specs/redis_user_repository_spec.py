from co import factory, user as u

from expects import expect, be_true, be_false, contain, equal

with describe('Redis User Repository'):

    with before.each:
        self.repository = factory.create_redis_user_repository()
        self.repository.clear()

    with context('when adding a user'):
        with before.each:
            self.nickname = '@foolano'

            self.user = u.User(self.nickname)
            self.user.follow_to('@mengano')
            self.user.publish_co('How is going dudes?')

            self.repository.put(self.user)

        with it('exists'):
            expect(self.repository.exists(self.nickname)).to(be_true)

        with it('has its following list'):
            user = self.repository.find_by_nickname(self.nickname)

            expect(user.following).to(equal(self.user.following))

        with it('has its cos list'):
            user = self.repository.find_by_nickname(self.nickname)

            expect(user.cos).to(equal(self.user.cos))

    with context('when looking for an unregistered user'):
        with it('returns false'):
            user = '@foolano'

            expect(self.repository.exists(user)).to(be_false)
