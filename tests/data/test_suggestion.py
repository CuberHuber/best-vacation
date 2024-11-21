import pytest
import datetime

from the_best_vacation.data import Suggestion


class TestSequence:

    def test_right(self):
        days = [datetime.date(2024, 12, 30), datetime.date(2024, 12, 31), datetime.date(2025, 1, 1), datetime.date(2025, 1, 2), datetime.date(2025, 1, 3), datetime.date(2025, 1, 4), datetime.date(2025, 1, 5)]
        vac = [datetime.date(2025, 1, 1)]


        assert Suggestion(days, vac)
