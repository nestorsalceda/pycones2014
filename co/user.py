class User(object):

    def __init__(self, nickname):
        self.nickname = nickname
        self._following = []

    def follow_to(self, nickname):
        self._following.append(nickname)

    @property
    def following(self):
        return self._following
