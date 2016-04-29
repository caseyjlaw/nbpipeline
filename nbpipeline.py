from ipywidgets import interact, FloatSlider, Text, Dropdown
import pickle, os
from functools import partial


def setstate(obj, dest):
    with open(dest, 'rw') as pkl:
        objorig = pickle.load(pkl)

        if objorig != obj:
            pickle.dump(obj, pkl)


def getstate(dest):
    obj = pickle.load(open(dest, 'r')) if os.path.exists(dest) else None


def stringstate(dest, description='Add Comment'):
    obj = getstate(dest)
    if not obj: obj = ''

    textc = Text(value=obj, description=description)
    setdest = partial(setstate, dest=dest)
    setdest.__name__ = 'setdest'

    hndl = interact(setdest, obj=textc, __manual=True)
