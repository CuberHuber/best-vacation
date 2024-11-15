import datetime

from the_best_vacation.data import Sequence
from the_best_vacation.utils import find_sequences, combinations


class BestVacation:
    """
    Реализация функции `F(D, W, v, P) -> d's`,
        где D - непрерывная серия дней (календарь);
        W - прерывная серия дней государственных выходных дней, отпусков и праздников;
        v - количество отпускных дней, которые мы можем использовать;
        `d's` - кортеж дней, на которые нужно взять отпуск.
    """

    def __init__(self, D: list[datetime.date], W: list[datetime.date], v: int):
        """

        :param D: непрерывная серия дней (календарь)
        :param W: прерывная серия дней государственных выходных дней, отпусков и праздников
        :param v: количество отпускных дней, которые мы можем использовать
        """
        self.calendar = D
        self.weekends = W
        self.free_days = v

        ...

    def suggestions(self):
        """Серия предложений - дни, на которые стоит взять отпуск"""
        # формирование списка выборки
        _temp_list = []
        for day in self.calendar:
            _temp_list.append(day in self.weekends)
        print("Initial _temp_list:", _temp_list)

        _combs = {}

        for comb in combinations(_temp_list, self.calendar, self.weekends, self.free_days):
            _combs[comb] = []
            # Последовательности более 1 повторения
            seqs = find_sequences(list(comb[0]), True)
            _seqs: list[Sequence] = []
            _max_seq = 0
            for seq in seqs:
                _seqs.append(seq)
                _max_seq = max(_max_seq, len(seq))
            for seq in seqs:
                if len(seq) == _max_seq:
                    _combs[comb].append(seq)
            # print(_max_seq, _combs[comb])

        # print(_combs.values())
        _all_seqs = []
        for __seqs in _combs.values():
            _all_seqs.extend(__seqs)
        _all_seqs.sort(key=lambda el: len(el))

        _new_all: list[Sequence] = []
        _m = max(_all_seqs, key=lambda _l: len(_l))
        for el_f in filter(lambda el: len(el) == len(_m), _all_seqs):
            _new_all.append(el_f)

        _out3 = []
        for _seq2 in tuple(set(_new_all)):
            _out2 = []
            for _d in self.calendar[_seq2.start:_seq2.end + 1]:
                if _d not in self.weekends:
                    _out2.append(_d)
            assert len(_out2) == self.free_days
            _out3.append(_out2)
            print(len(_seq2), _out2)
        return _out3
