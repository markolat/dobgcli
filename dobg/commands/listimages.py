import sys

sys.path.append('..')

import digitalocean
from digitalocean import DataReadError, TokenError

from dobg.helper.confighandler import ConfigHandler
from dobg.exceptions.configexceptions import InvalidTokenException


def list_images(args):
    """ Lists all of Droplets """

    token = ConfigHandler.get_config_setting('token')

    manager = digitalocean.Manager(token=token)

    try:
        images = manager.get_all_images()
    except (DataReadError, TokenError):
        raise InvalidTokenException

    result = '{:10}{:46}{:15}{:37}{}\n'.format('Id:', 'Name:', 'Distribution:', 'slug:', 'Regions:\n')
    for image in images:
        result += '{:<10}{:46}{:15}{:37}{}\n'.format(image.id, image.name, image.distribution, image.slug if image.slug else 'N/A', ', '.join(image.regions))

    print(result)

        
        
    
    