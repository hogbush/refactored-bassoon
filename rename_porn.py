#!/usr/bin/env python3

'''
Porn renamer.
'''

_SERIES = {
    'tf': 'TeenFidelity',
    'prvs': 'PrivateSociety',
    'girlsoutwest': 'GirlsOutWest',
    'tonightsgirlfriend': 'Tonights Girlfriend',
    'newsensations': 'NewSensations',
    'ted': 'Throated'
}

def _format_series(name):
    '''
    :param name: Series name from the ugly filename,
                 e.g. 'tf', 'tushy' or 'ted'.
    '''

    try:
        name = _SERIES[name]
    except KeyError:
        name = name.title()

    return name
