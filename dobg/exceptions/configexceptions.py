
class TokenException(Exception):
    """ """


class InvalidTokenException(TokenException):

    def __str__(self):
        return "Your Digital Ocean authentication token is invalid.\
                    \nPlease, set valid token with 'settoken' command."


class MissingTokenException(TokenException):

    def __str__(self):
        return "It seems like you haven't set up your Digital Ocean authentication token. \
                    \nPlease, set your token using 'settoken' command."