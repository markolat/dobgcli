import sys

sys.path.append('..')

import digitalocean
from digitalocean import DataReadError, TokenError

from dobg.helper.confighandler import ConfigHandler
from dobg.exceptions.configexceptions import InvalidTokenException
from dobg.exceptions.dropletexceptions import InvalidIdException


def delete_droplet(args):
    """ Destroys Droplet """
     
    token = ConfigHandler.get_config_setting('token')

    manager = digitalocean.Manager(token=token)

    try:
        droplet = manager.get_droplet(int(args.id))
    except (DataReadError, TokenError):
        raise InvalidTokenException
    except Exception: # cannot import NotFoundError here
        raise InvalidIdException

    droplet.destroy()
    print("You have successfuly destroyed Droplet!\
        \nId: {}, Name: {}, Size: {}, Image: {}, Region: {}".format(droplet.id, droplet.name, droplet.size_slug, 
                                                                                        droplet.image['slug'], droplet.region['slug']))
    
    