import pytest

from the_best_vacation.data import Sequence


class TestSequence:

    def test_right(self):
        lh = 0
        rh = 1

        try:
            Sequence(lh, rh)
        except Exception:
            assert False
        else:
            assert True

    def test_broken_1(self):
        lh = 0
        rh = 0

        try:
            Sequence(lh, rh)
        except AssertionError:
            assert True
        else:
            assert False

    def test_broken_2(self):
        lh = None
        rh = None

        try:
            Sequence(lh, rh)
        except AssertionError:
            assert True
        else:
            assert False

    def test_broken_3(self):
        lh = 1
        rh = None

        try:
            Sequence(lh, rh)
        except AssertionError:
            assert True
        else:
            assert False

    def test_right_2(self):
        lh = 1
        rh = 2

        try:
            Sequence(lh, rh)
        except Exception:
            assert False
        else:
            assert True

    def test_broken_4(self):
        lh = 6
        rh = 2

        try:
            Sequence(lh, rh)
        except Exception:
            assert True
        else:
            assert False

    def test_len(self):
        lh = 0
        rh = 2

        s = Sequence(lh, rh)
        assert len(s) == 3

    def test_len_2(self):
        lh = 0
        rh = 4

        s = Sequence(lh, rh)
        assert len(s) == 5

    def test_len_3(self):
        lh = 6
        rh = 10

        s = Sequence(lh, rh)
        assert len(s) == 5
