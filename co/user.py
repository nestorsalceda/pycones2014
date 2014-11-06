class User(object):

    def __init__(self, nickname):
        self.nickname = nickname
        self._following = []
        self._cos = []

    def follow_to(self, nickname):
        self._following.append(nickname)

    def publish_co(self, message):
        self._cos.append(message)

    @property
    def following(self):
        return self._following

    @property
    def cos(self):
        return self._cos
