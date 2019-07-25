import sys

sys.path.append('..')


class InvalidIdException(Exception):

    def __str__(self):
        return "Invalid Droplet ID."
