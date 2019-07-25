import sys

sys.path.append('..')

import argparse

from .commands.settoken import set_token
from .commands.createdroplet import create_droplet
from .commands.deletedroplet import delete_droplet
from .commands.listdroplets import list_droplets
from .commands.listsizes import list_sizes
from .commands.listimages import list_images

from .helper.confighandler import ConfigHandler
from .helper.exceptionhandler import ExceptionHandler

def main():

    # main parser
    parser = argparse.ArgumentParser(prog="dobg", description="", epilog="Use <command> --help to see how to use certain command.")

    # subparsers for commands
    commands = parser.add_subparsers(title="commands", metavar='')

    # createdroplet command
    createdroplet_command = commands.add_parser('createdroplet', help="Creates a Droplet")
    createdroplet_command.add_argument("name", help="Name of a droplet")
    createdroplet_command.add_argument("-r", "--region", default="fra1", help="The unique slug identifier for the region that you wish to deploy in.")
    createdroplet_command.add_argument("-i", "--image", default="ubuntu-16-04-x64", help="Unique slug identifier for public image")
    createdroplet_command.add_argument("-s", "--size", default="s-1vcpu-1gb", help="The unique slug identifier for the size that you wish to select for this Droplet.")
    createdroplet_command.set_defaults(func=create_droplet)

    # deletedroplet command
    deletedroplet_command = commands.add_parser('deletedroplet', help="Destroys a Droplet")
    deletedroplet_command.add_argument("id", type=int, help="Id that uniquely identifies a Droplet.")
    deletedroplet_command.set_defaults(func=delete_droplet)

    # listdroplets command
    listdroplets_command = commands.add_parser('listdroplets', help="Lists all Droplets")
    listdroplets_command.set_defaults(func=list_droplets)

    # listsizes command
    listsizes_command = commands.add_parser('listsizes', help="Lists all Sizes available")
    listsizes_command.set_defaults(func=list_sizes)

    # listimages command
    listimages_command = commands.add_parser('listimages', help="Lists all Images available")
    listimages_command.set_defaults(func=list_images)

    # settoken command
    settoken_command = commands.add_parser('settoken', help="Sets the authentication token in config file")
    settoken_command.add_argument('token', help="Authentication token provided by Digital Ocean")
    settoken_command.set_defaults(func=set_token)

    args = parser.parse_args()

    if len(args.__dict__) < 1:
        parser.print_help()
        parser.exit()

    try:
        args.func(args)
    except Exception as e:
        exception_handler = ExceptionHandler(e)
        exception_handler.handle()