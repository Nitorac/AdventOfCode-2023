from functools import reduce
from copy import deepcopy

IS_PART2 = True

data = []

data_item = []
for line in open('input', 'r').read().splitlines():
    line = line.strip()
    if line == '':
        data.append(data_item)
        data_item = []
        continue
    data_item.append([c for c in line])

if data_item:
    data.append(data_item)


def is_sym(grid, left, right):
    count = 1
    while left - count >= 0 and right + count < len(grid):
        diff = reduce(lambda cur, x: cur + (0 if x[0] == x[1] else 1), zip(grid[left - count], grid[right + count]), 0)
        if diff > 0:
            return False
        count += 1
    return True


def compare_syms(old, new):
    res = [True, True]
    diff = [{}, {}]
    for i in range(2):
        diff[i] = new[i].difference(old[i])
        if len(diff[i]) != 1:
            res[i] = False
    return diff if True in res else None


def find_reflection_with_smudges(grid):
    old = get_sym(grid)
    res_mut = None
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            mut = deepcopy(grid)
            mut[i][j] = '.' if mut[i][j] == '#' else '#'
            mut_sym = get_sym(mut)
            if diff := compare_syms(old, mut_sym):
                assert res_mut is None or res_mut == diff
                res_mut = diff
    return res_mut


def get_sym(grid):
    tr = [*zip(*grid)]
    potential_sym = []
    potential_sym_tr = []

    # Horizontal symetries
    for i in range(1, len(grid)):
        if reduce(lambda cur, x: cur + (0 if x[0] == x[1] else 1), zip(grid[i - 1], grid[i]), 0) == 0:
            potential_sym.append(i - 1)

    # Vertical symetries
    for i in range(1, len(tr)):
        if reduce(lambda cur, x: cur + (0 if x[0] == x[1] else 1), zip(tr[i - 1], tr[i]), 0) == 0:
            potential_sym_tr.append(i - 1)

    res = [set(), set()]
    for sym in potential_sym:
        if is_sym(grid, sym, sym + 1):
            res[0].add(sym)

    for sym in potential_sym_tr:
        if is_sym(tr, sym, sym + 1):
            res[1].add(sym)

    return res

total = 0
for i, mgrid in enumerate(data):
    res = find_reflection_with_smudges(mgrid) if IS_PART2 else get_sym(mgrid)
    if not res:
        print(f"data[{i}] is None")
        continue
    for e in res[0]:
        total += (e + 1) * 100
    for e in res[1]:
        total += (e + 1)

print(total)
