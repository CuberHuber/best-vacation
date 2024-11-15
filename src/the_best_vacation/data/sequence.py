import dataclasses


@dataclasses.dataclass
class Sequence:
    """
    Sequence represents a sequence of indexes.

    Rules:
        1. elements must not be repeated
        2. elements only by increasing

    Right sequence: [1, 2, 3, 4, 5]
    Wrong sequence: [-1, 0, 1, 2, 3]
    Wrong sequence: [1, 0, 2, 3, 1]
    """

    _lh: int
    _rh: int
    _len: int = None

    def __init__(self, lh: int, rh: int):
        assert lh is not None and rh is not None
        assert lh >= 0 and rh >= 1, "lh must be >= 0 and rh must be >= 1"
        assert lh < rh, "lh must be <= rh"
        self._lh = lh
        self._rh = rh

    def __len__(self) -> int:
        if self._len is None:
            self._len = self._rh - self._lh + 1
        return self._len

    def __hash__(self):
        return hash((self._lh, self._rh))
    
    @property
    def start(self) -> int:
        """The start index of the sequence."""
        return self._lh
    
    @property
    def end(self) -> int:
        """The finish index of the sequence."""
        return self._rh
