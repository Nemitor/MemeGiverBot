import math

searching_index = 100000
max_data = 1023
max_index = 100000

Cells = math.ceil(max_index / max_data)
print(f"Data Cells: {Cells} ")

data_per_depth = max_data


def calculate_depth(cell):
    if cell <= 0:
        return 0
    max_per_depth = 0
    i = 0
    while max_per_depth < cell:
        i += 1
        max_per_depth += 4 ** i
    return i


def cells_per_depth(depth):
    if depth <= 0:
        return 0
    max_per_depth = 0
    i = 0
    while i < depth:
        i += 1
        max_per_depth += 4 ** i
    return max_per_depth + 1


depth = calculate_depth(Cells)

print(f"Depth: {depth}")

print("===Path to target cell===")
target_cell = math.ceil(searching_index / max_data) - 1
print(f"Target cell : {target_cell}")


def calculate_index_path(cell):
    _cell = cell
    _depth = calculate_depth(_cell) - 1
    _cells_per_depth = cells_per_depth(_depth)
    _difference = _cell - _cells_per_depth
    _up_level_difference = _difference // 4
    print(f"Index path: {_difference % 4}")

    while _depth > 0:
        _depth -= 1
        _cells_per_depth = cells_per_depth(_depth)
        _cell = _cells_per_depth + _up_level_difference
        _difference = _cell - _cells_per_depth
        _up_level_difference = _difference // 4
        print(f"Index path: {_difference % 4}")



calculate_index_path(target_cell)
