from co import factory

from expects import expect, be_true, be_false

with describe('Redis User Repository'):

    with before.each:
        self.repository = factory.create_redis_user_repository()
        self.repository.clear()

    with it('adds a user'):
        user = '@foolano'

        self.repository.put(user)

        expect(self.repository.exists(user)).to(be_true)

    with context('when looking for an unregistered user'):
        with it('returns false'):
            user = '@foolano'

            expect(self.repository.exists(user)).to(be_false)
