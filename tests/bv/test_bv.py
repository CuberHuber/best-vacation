from data import dataset
from the_best_vacation import BestVacation


class TestBV:

    def test_result(self, dataset):
        for _set in dataset:
            _bv = BestVacation(_set.days, _set.weekends, _set.v)
            res = _bv.suggestions()
            assert len(res) == _set.res_len
