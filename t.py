#!/usr/bin/env python
import datetime
_DATETIME_FORMATS = [
    "%a %b %d %H:%M:%S %Y",
    "%Y-%m-%d %H:%M:%S",
    "%Y-%m-%d %H:%M",
    "%Y-%m-%dT%H:%M",
    "%Y%m%d %H:%M:%S",
    "%Y%m%d %H:%M",
    "%Y-%m-%d",
    "%Y%m%d",
    "%H:%M:%S",
    "%H:%M",
]

def _parse_datetime(value):
    for format in _DATETIME_FORMATS:
        try:
            return datetime.datetime.strptime(value, format)
        except ValueError:
            pass
    raise Error('Unrecognized date/time format: %r' % value)

_TIMEDELTA_ABBREVS = [
    ('hours', ['h']),
    ('minutes', ['m', 'min']),
    ('seconds', ['s', 'sec']),
    ('milliseconds', ['ms']),
    ('microseconds', ['us']),
    ('days', ['d']),
    ('weeks', ['w']),
]


a = _parse_datetime('2011-11-11')
print a
