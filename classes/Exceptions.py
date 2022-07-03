class AuthenticException(Exception):
    def __init__(self, user=None, username=None):
        self.user = user
        self.username = username


class IncorrectPassword(AuthenticException):
    def __init__(self):
        super().__init__()
        print("Podane hasło jest niepoprawne.")


class IncorrectUsername(AuthenticException):
    def __init__(self):
        super().__init__()
        print("Podany username jest niepoperawny.")


class NotLoggedError(AuthenticException):
    def __init__(self):
        super().__init__()
        print("Użytkownik niezalogowany.")
    pass


class PasswordTooShort(AuthenticException):
    def __init__(self):
        super().__init__()
        print("Za krótkie hasło.")


class UsernameAlreadyExists(AuthenticException):
    def __init__(self):
        super().__init__()
        print("Użytkownik istnieje")


class NotPermittedError(AuthenticException):
    def __init__(self):
        super().__init__()
        print("Brak uprawnień.")
