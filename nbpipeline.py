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


def filterdata(data, plinds, threshold, ignorestr, thresh0=6., thresh1=7.):
    """ Iteratively filter bad times and set indices for later plotting """

    ignoret = parseignoret(ignorestr)
    plinds['cir'] = interactive.calcinds(data, thresh0, ignoret=ignoret) # positive cands
    plinds['cro'] = interactive.calcinds(data, -1*thresh0, ignoret=ignoret) # negative cands
    plinds['edg'] = interactive.calcinds(data, thresh1, ignoret=ignoret) # cands with png plots
    sortinds = sorted(set(plinds['cir'] + plinds['cro'] + plinds['edg']))
    print('Selected {} ({} linked) points.'.format(len(sortinds), len(plinds['edg'])))
    
    print('Estimated total on target time: {} s\n'.format(interactive.calcontime(
        data, inds=plinds['cir']+plinds['cro']+plinds['edg'])))
    
    # these must get get rescaled when cands are ignored
    data['zs'] = interactive.normprob(d, data['snrs'], inds=sortinds)   

    # print high 1s bin counts
    hight, highcount = interactive.findhight(data, ignoret=ignoret, threshold=threshold)
    if len(hight):
        print('High times \t High counts:')
        for i in range(len(hight)):
              print('{0}\t{1}'.format(hight[i], highcount[i]))
    else:
        print('No high 1s bin counts.')
    print('\n')

    # print high cands and their times
    biginds = np.argsort(data['abssnr'][sortinds])[-5:]    
    print('Top 5 abs(snr) candidates and times:')
    for ind in biginds[::-1]:
        print(data['snrs'][sortinds][ind], data['time'][sortinds][ind])
    print('\n')


def parseignoret(ignorestr):
    if ',' in ignorestr:
        ignorelist = ignorestr.split(',')
        assert (len(ignorelist)/2.).is_integer(), 'ignorestr be pairs of comma-delimited values.'
        ignoret = [(int(ignorelist[i]), int(ignorelist[i+1])) for i in range(0, len(ignorelist), 2)]
    else:
        ignoret = []
    return ignoret        


def displayplot(plottype, sizespec, url_path='http://www.aoc.nrao.edu/~claw/plots'):
    """ Generate interactive plot """

    plotdict = {'dmt': interactive.plotdmt, 'norm': interactive.plotnorm,
               'loc': interactive.plotloc, 'stat': interactive.plotstat,
               'all': interactive.plotall}
    sizedict = {'dmt': [900,500], 'norm': [700, 700], 'loc': [700,700],
                'stat': [700,700]}

    sortinds = sorted(set(plinds['cir'] + plinds['cro'] + plinds['edg']))
    sizesrc, plaw = sizespec.split('_')
    data['sizes'] = interactive.calcsize(data[sizesrc], inds=sortinds, plaw=int(plaw))

    if plottype != 'all':
        wid, hei = sizedict[plottype]
        pl = plotdict[plottype](data, circleinds=plinds['cir'], crossinds=plinds['cro'],
                                edgeinds=plinds['edg'], url_path=url_path,
                                fileroot=fileroot, plot_width=wid, plot_height=hei)
    else:
        pl = interactive.plotall(data, circleinds=plinds['cir'], crossinds=plinds['cro'],
                                 edgeinds=plinds['edg'], url_path=url_path,
                                 fileroot=fileroot)
    hdl = show(pl)

