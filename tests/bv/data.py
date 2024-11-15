import dataclasses
import datetime

import pytest

from the_best_vacation.data import Suggestion


@dataclasses.dataclass
class TestSet:
    days: list[datetime.date]
    weekends: list[datetime.date]
    v: int

    res_len: int
    suggestions: list[Suggestion] = None


@pytest.fixture
def dataset() -> list[TestSet]:

    return [
        TestSet(
            [datetime.date(2024, 11, 1), datetime.date(2024, 11, 2), datetime.date(2024, 11, 3), datetime.date(2024, 11, 4), datetime.date(2024, 11, 5)],
            [datetime.date(2024, 11, 2), datetime.date(2024, 11, 3)],
            1,
            2
        ),
        TestSet(
            [datetime.date(2024, 11, 1), datetime.date(2024, 11, 2), datetime.date(2024, 11, 3),
             datetime.date(2024, 11, 4), datetime.date(2024, 11, 5), datetime.date(2024, 11, 6)],
            [datetime.date(2024, 11, 2), datetime.date(2024, 11, 3)],
            1,
            2
        ),
        TestSet(
            [datetime.date(2024, 11, 1), datetime.date(2024, 11, 2), datetime.date(2024, 11, 3),
             datetime.date(2024, 11, 4), datetime.date(2024, 11, 5), datetime.date(2024, 11, 6)],
            [datetime.date(2024, 11, 2), datetime.date(2024, 11, 3), datetime.date(2024, 11, 5)],
            1,
            1
        )
    ]
