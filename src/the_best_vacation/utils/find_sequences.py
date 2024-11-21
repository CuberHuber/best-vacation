from functools import cache

from the_best_vacation.data import Sequence


@cache
def find_sequences(arr: tuple, target) -> list[Sequence]:
    sequences = []
    current_count = 0
    start_index = -1

    for i in range(len(arr)):
        if arr[i] == target:
            if current_count == 0:
                start_index = i # remember seq start
            current_count += 1
        else:
            if current_count > 1 and start_index < i-1:  # current len seq > 0
                sequences.append(Sequence(start_index, i - 1))
            current_count = 0  # Сбрасываем счетчик

    # check last seq
    if current_count > 1 and len(arr) - 1 < current_count:
        sequences.append(Sequence(start_index, len(arr) - 1))

    return sequences
