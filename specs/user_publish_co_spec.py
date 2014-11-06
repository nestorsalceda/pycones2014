from co import services, repositories, errors, user as u

from expects import expect, contain, raise_error
from doublex import Spy, when
from doublex_expects import have_been_called

with description('Publish a co for a user'):

    with before.each:
        self.nickname = '@foolano'
        self.co = 'que pasa co?'
        self.repository = Spy(repositories.UserRepository)
        self.service = services.UsersService(self.repository)

    with context('when publishing a co'):
        with before.each:
            when(self.repository).exists(self.nickname).returns(True)
            when(self.repository).find_by_nickname(self.nickname).returns(u.User(self.nickname))

            self.service.publish_co(self.nickname, self.co)

        with it('refresh user data in repository'):
            expect(self.repository.put).to(have_been_called)

        with it('exists in users cos list'):
            expect(self.service.cos_for(self.nickname)).to(contain(self.co))

    with context('when user is not registered'):
        with it('raises an error'):
            expect(lambda: self.service.publish_co(self.nickname, self.co)).to(raise_error(errors.UserDoesNotExistError))


