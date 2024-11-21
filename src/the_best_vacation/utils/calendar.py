import datetime
from copy import copy
from functools import cache


class CalGen:

    def __init__(self, start: datetime.date, end: datetime.date):
        assert start < end
        self._start = start
        self._end = end

    @property
    @cache
    def days(self) -> list[datetime.date]:
        _indate = copy(self._start)
        _out = []
        while _indate <= self._end:
            _out.append(_indate)
            _indate += datetime.timedelta(days=1)
        return _out
