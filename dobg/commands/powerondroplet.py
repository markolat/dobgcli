import sys

sys.path.append('..')

import digitalocean
from digitalocean import DataReadError, TokenError

from dobg.helper.confighandler import ConfigHandler
from dobg.exceptions.configexceptions import InvalidTokenException
from dobg.exceptions.dropletexceptions import InvalidIdException


def power_on_droplet(args):
    """ Turns on a Droplet with given id """
     
    token = ConfigHandler.get_config_setting('token')

    manager = digitalocean.Manager(token=token)

    try:
        droplet = manager.get_droplet(int(args.id))
    except (DataReadError, TokenError):
        raise InvalidTokenException
    except Exception: # cannot import NotFoundError here
        raise InvalidIdException

    action = droplet.power_on()
    print("Droplet power-on status: {}\n".format(action['action']['status']))
    
    