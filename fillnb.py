#!/usr/bin/env python

# Quick script to compile all jupyter notebooks for realfast
# baseinteract.ipynb notebook designed to compile without interaction, but 
# also has interact mode for refined analysis

from sys import argv
import os
from subprocess import call

directory = argv[1].rstrip('/')
os.environ['sdmdir'] = directory

print('Running on {0}'.format(directory))
if os.path.exists(directory):
    cmd = 'jupyter nbconvert baseinteract.ipynb --output {0}/{0}.ipynb --to notebook --execute --allow-errors --ExecutePreprocessor.timeout=3600'.format(directory).split(' ')
    print('Running nbconvert...')
    status = call(cmd)

    cmd = 'jupyter trust {0}/{0}.ipynb'.format(directory).split(' ')
    status = call(cmd)
    print('Done with {0}'.format(directory))

