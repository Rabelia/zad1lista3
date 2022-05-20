class AuthenticException(Exception):
    def __init__(self, user=None, username=None):
        self.user = user
        self.username = username


class IncorrectPassword(AuthenticException):
    def __init__(self):
        print("Podane hasło jest niepoprawne.")


class IncorrectUsername(AuthenticException):
    def __init__(self):
        print("Podany username jest niepoperawny.")


class NotLoggedError(AuthenticException):
    pass


class PasswordTooShort(AuthenticException):
    pass


class UsernameAlreadyExists(AuthenticException):
    def __init__(self):
        print("Użytkownik istnieje")


class NotPermittedError(AuthenticException):
    pass
