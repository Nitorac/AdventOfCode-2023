from itertools import combinations

IS_PART2 = True

grid = []
empty_lines = []
empty_cols = []
for i, line in enumerate(open('input', 'r').read().splitlines()):
    if all(map(lambda c: c == '.', line)):
        empty_lines.append(i)
    grid.append([c for c in line])

for j in range(len(grid[0]) - 1, -1, -1):
    column = [line[j] for line in grid]
    if all(map(lambda c: c == '.', column)):
        empty_cols.append(j)

print(empty_lines)
print(empty_cols)

galaxies = []
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == '#':
            galaxies.append((i, j))


def compute_distance(g1, g2):
    res = abs(g2[0] - g1[0]) + abs(g2[1] - g1[1])
    # Add empty lines
    for line in empty_lines:
        if min(g1[0], g2[0]) < line < max(g1[0], g2[0]):
            res += 1_000_000 - 1 if IS_PART2 else 1
    for col in empty_cols:
        if min(g1[1], g2[1]) < col < max(g1[1], g2[1]):
            res += 1_000_000 - 1 if IS_PART2 else 1
    return res


res = 0
for ga1, ga2 in combinations(range(len(galaxies)), 2):
    res += compute_distance(galaxies[ga1], galaxies[ga2])

print(res)
