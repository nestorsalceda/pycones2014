from co import factory, user as u

from expects import expect, be_true, be_false, be_none

with describe('Redis User Repository'):

    with before.each:
        self.repository = factory.create_redis_user_repository()
        self.repository.clear()

    with it('adds a user'):
        nickname = '@foolano'
        user = u.User(nickname)

        self.repository.put(user)

        expect(self.repository.exists(nickname)).to(be_true)
        expect(self.repository.find_by_nickname(nickname)).not_to(be_none)


    with context('when looking for an unregistered user'):
        with it('returns false'):
            nickname = '@foolano'

            expect(self.repository.exists(nickname)).to(be_false)
