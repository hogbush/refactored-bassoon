#!/usr/bin/env python3

import re
from typing import Dict, Optional

'''
Porn renamer.
'''

_SERIES: Dict[str, str] = {
    'tf': 'TeenFidelity',
    'prvs': 'PrivateSociety',
    'girlsoutwest': 'GirlsOutWest',
    'tonightsgirlfriend': 'Tonights Girlfriend',
    'newsensations': 'NewSensations',
    'ted': 'Throated'
}

_SPECIAL_WORDS: Dict[str, str] = {
    'bts': 'BTS',  # behind the scenes
    'and': 'and'
}


def _format_series(name: str) -> str:
    '''
    :param name: Series name from the ugly filename,
                 e.g. 'tf', 'tushy' or 'ted'.
    '''

    try:
        name = _SERIES[name]
    except KeyError:
        name = name.title()

    return name


def _reformat_filename(name: str) -> str:
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


def _format_date(year: str, month: str, day: str) -> str:
    '''
    :param year: Year as two digits, e.g. '17'.
    :param month: Month as two digits, e.g. '02'.
    :param day: Day as two digits, e.g. '09'.
    '''

    return f'20{year}-{month}-{day}'


def _format_extension(extension: str) -> str:
    return extension.lower()


def format_name(name: str) -> Optional[str]:
    '''
    :param name: Full file name, with extension, e.g.
        'vixen.17.09.26.jill.kassidy.and.olivia.nova.mp4'
    '''

    NAME_REGEX = r'(.+?)\.(\d\d)\.(\d\d)\.(\d\d)\.(.+)\.(.+)'

    match = re.fullmatch(NAME_REGEX, name)
    if not match:
        return None

    series, y, m, d, title, extension = match.groups()

    series = _format_series(series)
    date = _format_date(y, m, d)
    title = _reformat_filename(title)
    extension = _format_extension(extension)

    new_name = f'[{series}] {date} {title}.{extension}'

    return new_name

