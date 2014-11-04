from collections import defaultdict

from expects import expect, be_true, contain

class FollowService(object):

    def __init__(self):
        self._follows = defaultdict(list)

    def follow_to(self, user, target):
        self._follows[user].append(target)

    def is_following_to(self, user, other):
        return other in self._follows[user]

    def follows_to(self, user):
        return self._follows[user]

with description('Follow user'):
    with before.each:
        self.user = '@foolano'
        self.other_user = '@da_kewl_guru'
        self.service = FollowService()

    with it('follows a user'):
        self.service.follow_to(self.user, self.other_user)

        expect(self.service.is_following_to(self.user, self.other_user)).to(be_true)


    with it('allows to get all users followed by a user'):
        self.service.follow_to(self.user, self.other_user)

        expect(self.service.follows_to(self.user)).to(contain(self.other_user))
