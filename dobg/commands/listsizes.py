import sys

sys.path.append('..')

import digitalocean
from digitalocean import DataReadError, TokenError

from dobg.helper.confighandler import ConfigHandler
from dobg.exceptions.configexceptions import InvalidTokenException


def list_sizes(args):
    """ Lists all of Droplets """

    token = ConfigHandler.get_config_setting('token')

    manager = digitalocean.Manager(token=token)

    try:
        sizes = manager.get_all_sizes()
    except (DataReadError, TokenError):
        raise InvalidTokenException

    result = '{:18}{:<10}{:<8}{:<8}{:<20}{}\n'.format('Slug:', 'Memory:', 'CPUs:', 'Disk:', 'Price per month:', 'Regions:\n')
    for size in sizes:
        result += '{:18}{:<10}{:<8}{:<8}{:<20}{}\n'.format(size.slug, size.memory, size.vcpus, size.disk, size.price_monthly, ', '.join(size.regions))

    print(result)

        
        
    
    