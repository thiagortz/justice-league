from werkzeug.security import safe_str_cmp


class User(object):
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def get_users(self):
        return [
            User(1, 'AQUAMAN', 'JusticeLeague')
        ]

    @staticmethod
    def authenticate(username, password):
        user = User('2', str(username).upper().replace(" ", ""), password)
        if user.get_users()[0].username == user.username and safe_str_cmp(user.get_users()[0].password.encode('utf-8'),
                                                                          user.password.encode('utf-8')):
            return user.get_users()[0]

    @staticmethod
    def identity(payload):
        return User(1, 'AQUAMAN', 'JusticeLeague')
