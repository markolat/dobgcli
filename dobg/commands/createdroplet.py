import sys

sys.path.append('..')

import digitalocean

from dobg.helper.confighandler import ConfigHandler


def create_droplet(args):
    """ Creates Droplet """    
    
    token = ConfigHandler.get_config_setting('token')
    
    droplet = digitalocean.Droplet(token=token,
                                    name=args.name,
                                    region=args.region,
                                    image=args.image,
                                    size_slug=args.size,
                                    backups=True)

    droplet.create()

    print("You have successfuly created Droplet!\
        \nId: {}, Name: {}, Size: {}, Image: {}, Region: {}".format(droplet.id, droplet.name, droplet.size_slug, 
                                                                                        droplet.image, droplet.region))
    
    