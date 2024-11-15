import dataclasses
import datetime


@dataclasses.dataclass
class Suggestion:
    """
    Suggestion represents an uninterrupted holiday sequence and set of days for taken vacation.
    """

    all_days: list[datetime.date]
    vacation_days: list[datetime.date]

    def __init__(self, days: list[datetime.date], vacation: list[datetime.date]):
        assert isinstance(days, list) and isinstance(vacation, list)
        assert len(vacation) <= len(days)
        assert set(vacation) in set(days)
        self.all_days = days
        self.vacation_days = vacation
