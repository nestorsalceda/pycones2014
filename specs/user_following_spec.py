from co import services

from expects import expect, be_true, contain

with description('Follow user'):
    with before.each:
        self.user = '@foolano'
        self.other_user = '@da_kewl_guru'
        self.service = services.UsersService()

    with it('follows a user'):
        self.service.follow_to(self.user, self.other_user)

        expect(self.service.is_following_to(self.user, self.other_user)).to(be_true)


    with it('allows to get all users followed by a user'):
        self.service.follow_to(self.user, self.other_user)

        expect(self.service.follows_to(self.user)).to(contain(self.other_user))
