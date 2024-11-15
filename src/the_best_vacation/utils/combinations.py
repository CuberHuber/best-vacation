import itertools

def combinations(_t: list, _D: list, _W: list, _v: int) -> list:
    out = []

    _v_count = int(_v)
    indices_to_change = [i for i in range(len(_D)) if _D[i] not in _W]

    # Перебор всех комбинаций индексов, которые можно изменить
    for comb in itertools.combinations(indices_to_change, min(_v_count, len(indices_to_change))):
        temp_list_copy = _t.copy()  # Создаем копию _temp_list для каждого сочетания
        for index in comb:
            temp_list_copy[index] = True  # Устанавливаем True для выбранных индексов
        # print("Modified _temp_list for combination", comb, ":", temp_list_copy)
        out.append((tuple(temp_list_copy), tuple(comb)))
    return out