#!/bin/sh

cd /home/markolat/repos/dobgcli;

rm -rf build/ dist/ dobg.egg-info/;

python setup.py install 
