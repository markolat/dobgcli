# DOBGCLI
---
Command line tool for easier management of your Digital Ocean droplets.

## Getting started
---
### Prerequisities
You will need to install [Python3](https://www.python.org/downloads/). Pip3 should be included in Python3 installation. Otherwise, install [pip3](https://pip.pypa.io/en/stable/installing/) manually.

### Installing
Use `pip3 install dobg` to install dobgcli globally or `pip install dobg` inside your virtual environment. Make sure, though, that virtual environment is using Python3.

### Start using dobgcli
This command will display general help message where you can see all subcommands and what they're used for:
```
dobg [-h]
```
You will need to set up config file with your Digital Ocean token:
```
dobg settoken <your_token>
```
After that, you will be able to use all other subcommands.

## Subcommands
---
### List of subcommands:
- `settoken` sets the user's Digital Ocean token in config file;
- `createdroplet` creates new droplet;
- `deletedroplet` destroys a droplet;
- `listdroplets` lists all of user's droplets;
- `listsizes` lists all available sizes;
- `listimages` lists all available images;
