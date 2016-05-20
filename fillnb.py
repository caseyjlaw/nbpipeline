#!/usr/bin/env python

# Example of command-line executable to compile a jupyter notebook
# nbpipeline model allows a base.ipynb (a pipeline script in ipynb format)
# to be compiled into a data product as ipynb and html.
# nbpipeline state object also allows for distributed interaction by saving state.

from sys import argv
import os
from subprocess import call

# define variable to be passed to notebook (which retrieves it from os.environ)
filename = argv[1]
os.environ['filename'] = filename

print('Compiling notebook for {0}'.format(filename))
cmd = 'jupyter nbconvert base.ipynb --output {0}.ipynb --to notebook --execute --allow-errors --ExecutePreprocessor.timeout=3600'.format(filename).split(' ')
status = call(cmd)

# trust notebook to allow it run embedded js (like some bokeh plots)
cmd = 'jupyter trust {0}.ipynb'.format(filename).split(' ')
status = call(cmd)

# convert to html for quick look without interaction
cmd = 'jupyter nbconvert {0}.ipynb --to html --output {0}.html'.format(fileroot).split(' ')
status = call(cmd)

print('Finished compiling notebook for {0}'.format(filename))

