import sys

sys.path.append('..')

from digitalocean import DataReadError

# must import full path to the exception
from dobg.exceptions.dropletexceptions import InvalidIdException 
from dobg.exceptions.configexceptions import TokenException


class ExceptionHandler:
    
    def __init__(self, exception):
        self.exception = exception

    
    # this function for now does the same job for every kind of exception (only prints it's message).
    def handle(self):
        """ Handles thrown exceptions from main script """

        if isinstance(self.exception, TokenException):
            print(self.exception)

        elif isinstance(self.exception, InvalidIdException):
            print(self.exception)
        
        else:
            print(self.exception)
        