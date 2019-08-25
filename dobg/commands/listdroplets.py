import sys

sys.path.append('..')

import digitalocean
from digitalocean import DataReadError, TokenError

from dobg.helper.confighandler import ConfigHandler
from dobg.exceptions.configexceptions import InvalidTokenException


def list_droplets(args):
    """ Lists all of Droplets """

    token = ConfigHandler.get_config_setting('token')

    manager = digitalocean.Manager(token=token)
    
    try:
        droplets = manager.get_all_droplets()
    except (DataReadError, TokenError):
        raise InvalidTokenException

    if len(droplets) == 0:
        print('No droplets.')
        return

    # make a helper function that will accept droplet and format print like this
    result = '{:15}{:40}{:10}{:18}{:37}{}'.format('ID:', 'Name:', 'Region:', 'Size:', 'Image:', 'Status:\n')
    for droplet in droplets:
        image = droplet.image['slug'] if droplet.image['slug'] else 'None' # instead of doing '!s' in format parenthesis (e.g. {!s:37})
        result += '{:<15}{:40}{:10}{:18}{:37}{}\n'.format(droplet.id, droplet.name, droplet.region['slug'], droplet.size_slug, image, droplet.status)
        
    print(result)

        
        
    
    