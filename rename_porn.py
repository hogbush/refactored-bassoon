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

_SPECIAL_WORDS = {
    'bts': 'BTS',  # behind the scenes
    'and': 'and'
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


def _reformat_filename(name):
    '''
    Pretty-format the filename.

    :param name: The filename with dots, without the extension.
        Example: "vixen.17.09.26.jill.kassidy.and.olivia.nova.mp4".
    '''

    words = []
    for word in name.split('.'):
        try:
            word = _SPECIAL_WORDS[word]
        except KeyError:
            word = word.title()
        words.append(word)

    new_name = ' '.join(words)

    return new_name


def _format_date(year: str, month: str, day: str):
    '''
    :param year: Year as two digits, e.g. '17'.
    :param month: Month as two digits, e.g. '02'.
    :param day: Day as two digits, e.g. '09'.
    '''

    return f'20{year}-{month}-{day}'
