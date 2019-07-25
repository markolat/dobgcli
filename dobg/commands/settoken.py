import sys

sys.path.append('..')

from dobg.helper.confighandler import ConfigHandler


def set_token(args):
    """ Sets a Digital Ocean authentication token in configuration file """

    answer = input('Are you sure you want to set this token? (yes/no)\n\nToken: {}\n\n'.format(args.token))
    print()
    
    if answer in ('y', 'Y', 'yes', 'YES', 'Yes'):
        ConfigHandler.set_config_setting('token', args.token)