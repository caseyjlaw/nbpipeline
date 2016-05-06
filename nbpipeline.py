from ipywidgets import interact, FloatSlider, Text, Dropdown, fixed
import pickle, os
from rtpipe import interactive


def save(obj, label):
    """ Save or update obj as pkl file with name label """

    # initialize hidden state directory
    if not os.path.exists('.nbpipeline'): os.mkdir('.nbpipeline')

    # read obj, if it exists
    objloc = '.nbpipeline/{0}'.format(label)
    if os.path.exists(objloc):
        with open(objloc, 'r') as pkl:
            objorig = pickle.load(pkl)

        # if obj is different from saved obj, then update saved obj
        if objorig != obj:
            with open(objloc, 'w') as pkl:
                pickle.dump(obj, pkl)

    # if obj file not there, initialize it
    else:
        with open(objloc, 'w') as pkl:
            pickle.dump(obj, pkl)


def read(label):
    """ Read obj with give label from hidden state directory """

    objloc = '.nbpipeline/{0}'.format(label)
    if os.path.exists(objloc):
        obj = pickle.load(open(objloc, 'r')) 
    else:
        obj = None

    return obj


def list():
    """ List names of stored objects """

    print(os.listdir('.nbpipeline/'))


def setText(label, default='', description='Set Text'):
    """ Set text in a notebook pipeline (via interaction or with nbconvert) """

    obj = read(label)
    if not obj: obj=default

    textw = Text(value=obj, description=description)
    hndl = interact(save, obj=textw, label=fixed(label), __manual=True)


def setFloat(label, default=0, min=-20, max=20, description='Set Float'):
    """ Set float in a notebook pipeline (via interaction or with nbconvert) """

    obj = read(label)
    if not obj: obj=default

    floatw = FloatSlider(value=obj, min=min, max=max, description=description)
    hndl = interact(save, obj=floatw, label=fixed(label), __manual=True)    


def setDropdown(label, default=None, options=[], description='Set Dropdown'):
    """ Set float in a notebook pipeline (via interaction or with nbconvert) """

    obj = read(label)
    if not obj: obj=default

    dropdownw = Dropdown(value=obj, options=options, description=description)
    hndl = interact(save, obj=dropdownw, label=fixed(label), __manual=True)    
