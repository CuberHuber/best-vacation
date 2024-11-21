import datetime
from the_best_vacation.data import Suggestion
from the_best_vacation.utils import find_sequences, combinations


class BestVacation:
    """
    Implementation of the function `F(D, W, v, P) -> d's`,
        where D - continuous series of days (calendar);
        W - discontinuous series of public holidays, vacations, and celebrations;
        v - number of vacation days that can be used;
        `d's` - tuple of days to take vacation.
    """

    def __init__(self, D: list[datetime.date], W: list[datetime.date], v: int):
        """
        :param D: continuous series of days (calendar)
        :param W: discontinuous series of public holidays, vacations, and celebrations
        :param v: number of vacation days that can be used
        """
        self.calendar = D
        self.weekends = set(W)  # Use a set for faster lookups
        self.free_days = v

    def suggestions(self) -> list[Suggestion]:
        """Series of suggestions - days to take vacation"""
        # Create a boolean list indicating whether each day is a weekend
        is_weekend = [day in self.weekends for day in self.calendar]

        # Store sequences of non-weekend days that can be taken as vacation
        _combs = {}

        # Generate combinations and find sequences
        for comb in combinations(is_weekend, self.calendar, list(self.weekends), self.free_days):
            seqs = find_sequences(tuple(comb[0]), True)
            max_length = max((len(seq) for seq in seqs), default=0)
            _combs[comb] = [seq for seq in seqs if len(seq) == max_length]

        # Flatten and sort sequences by length
        all_seqs = [seq for seq_list in _combs.values() for seq in seq_list]
        all_seqs.sort(key=len)

        # Find the longest sequences and filter out non-weekend days
        max_seq_length = len(all_seqs[-1]) if all_seqs else 0
        print([seq for seq in set(all_seqs) if len(seq) == max_seq_length])

        _out = []
        for seq in set(all_seqs):
            if len(seq) == max_seq_length:
                _all_days = self.calendar[seq.start:seq.end + 1]
                _vac_days = [day for day in _all_days if day not in self.weekends]
                _out.append(Suggestion(_all_days, _vac_days))

        return _out
