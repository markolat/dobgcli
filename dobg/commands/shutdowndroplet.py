import sys

sys.path.append('..')

import digitalocean
from digitalocean import DataReadError, TokenError

from dobg.helper.confighandler import ConfigHandler
from dobg.exceptions.configexceptions import InvalidTokenException
from dobg.exceptions.dropletexceptions import InvalidIdException


def shutdown_droplet(args):
    """ Turns off a Droplet with given id """
     
    token = ConfigHandler.get_config_setting('token')

    manager = digitalocean.Manager(token=token)

    try:
        droplet = manager.get_droplet(int(args.id))
    except (DataReadError, TokenError):
        raise InvalidTokenException
    except Exception: # cannot import NotFoundError here
        raise InvalidIdException

    action = droplet.shutdown()
    print("Droplet shutdown status: {}\n".format(action['action']['status']))
    
    