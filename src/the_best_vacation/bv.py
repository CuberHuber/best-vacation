import copy
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

    def __init__(self, D: list[datetime.date], W: list[datetime.date], v: int, lazy: bool = False):
        """
        :param D: continuous series of days (calendar)
        :param W: discontinuous series of public holidays, vacations, and celebrations
        :param v: number of vacation days that can be used
        :param lazy: if True, only consider continuous sequences of free days
        """
        self.calendar = D
        self.weekends = set(W)  # Use a set for faster lookups
        self.free_days = v
        self.lazy = lazy

    def suggestions(self) -> list[Suggestion]:
        """Series of suggestions - days to take vacation"""
        # Store sequences of non-weekend days that can be taken as vacation
        _combs = self._combinations()

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

    def _find_continuous_sequences(self, indices):
        """Find continuous sequences of indices."""
        sequences = []
        current_sequence = []

        for i in range(len(indices)):
            if i == 0 or indices[i] == indices[i - 1] + 1:
                current_sequence.append(indices[i])
            else:
                if current_sequence:
                    sequences.append(current_sequence)
                current_sequence = [indices[i]]

        if current_sequence:
            sequences.append(current_sequence)

        return sequences

    def _combinations(self):
        # Create a boolean list indicating whether each day is a weekend
        is_weekend = [day in self.weekends for day in self.calendar]

        # Store sequences of non-weekend days that can be taken as vacation
        _combs = {}
        combs = []

        if self.lazy:
            _sub_sequence = [False] * self.free_days
            for i in range(len(is_weekend) - self.free_days):
                if is_weekend[i:i + self.free_days] == _sub_sequence:
                    _new_weekend = copy.copy(is_weekend)
                    _new_weekend[i:i + self.free_days] = [True]*self.free_days
                    combs.append(tuple(_new_weekend))
        else:
            # Generate combinations and find sequences
            for comb in combinations(is_weekend, self.calendar, list(self.weekends), self.free_days):
                combs.append(tuple(comb[0]))

        for _c in combs:
            seqs = find_sequences(_c, True)
            max_length = max((len(seq) for seq in seqs), default=0)
            _combs[_c] = [seq for seq in seqs if len(seq) == max_length]

        return _combs
