from pprint import pprint
from copy import deepcopy

data = []

for mline in open('input', 'r').read().splitlines():
    data.append([c for c in mline])

size_i = len(data)
size_j = len(data[0])


def tilt_direction(grid, direction):
    """
    :param grid:
    :param direction: 0 for North, 1 for West, 2 for South, 3 for East
    :return:
    """
    if direction < 2:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 'O':
                    if direction == 0:
                        k = i - 1
                        while k >= 0 and grid[k][j] == '.':
                            k -= 1
                        grid[i][j] = '.'
                        grid[k + 1][j] = 'O'
                    elif direction == 1:
                        k = j - 1
                        while k >= 0 and grid[i][k] == '.':
                            k -= 1
                        grid[i][j] = '.'
                        grid[i][k + 1] = 'O'
    else:
        for i in range(len(grid) - 1, -1, -1):
            for j in range(len(grid[0]) - 1, -1, -1):
                if grid[i][j] == 'O':
                    if direction == 2:
                        k = i + 1
                        while k < size_i and grid[k][j] == '.':
                            k += 1
                        grid[i][j] = '.'
                        grid[k - 1][j] = 'O'
                    elif direction == 3:
                        k = j + 1
                        while k < size_j and grid[i][k] == '.':
                            k += 1
                        grid[i][j] = '.'
                        grid[i][k - 1] = 'O'


def make_cycle(grid):
    tilt_direction(grid, 0)
    tilt_direction(grid, 1)
    tilt_direction(grid, 2)
    tilt_direction(grid, 3)


def compute_weight(grid):
    total_lines = len(grid)
    res = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'O':
                res += total_lines - i
    return res


loops = []
found_loop = None

for i in range(1_000_000_000):
    make_cycle(data)
    for k, loop in enumerate(loops):
        if data == loop:
            print(f"Loop found from {k} to {i}")
            found_loop = (k, i)
            break
    if found_loop is not None:
        break
    loops.append(deepcopy(data))

loop_len = found_loop[1] - found_loop[0]

# '(Ending cycles) - 1' because we stopped after the first cycle in the loop
for i in range((1_000_000_000 - found_loop[0]) % loop_len - 1):
    make_cycle(data)

pprint(compute_weight(data))
