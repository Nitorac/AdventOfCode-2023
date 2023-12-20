data = []

IS_PART2 = True

maps = {
    "R": (0, 1),
    "D": (1, 0),
    "L": (0, -1),
    "U": (-1, 0),
}

maps_part2 = ["R", "D", "L", "U"]

for line in open('input', 'r').read().splitlines():
    splitted = line.split()
    if IS_PART2:
        length = int(splitted[2][2:7], 16)
        direction = maps[maps_part2[int(splitted[2][7:8])]]
        data.append((direction, length, splitted[2][2:8]))
    else:
        data.append((maps[splitted[0]], int(splitted[1]), splitted[2][2:8]))


def shoelace_area(i_list, j_list):
    a1, a2 = 0, 0
    i_list.append(i_list[0])
    j_list.append(j_list[0])
    for j in range(len(i_list) - 1):
        a1 += i_list[j] * j_list[j + 1]
        a2 += j_list[j] * i_list[j + 1]
    return abs(a1 - a2) // 2


perimeter = 0
pivots = [(0, 0)]

for (i, j), count, color in data:
    perimeter += count
    pivots.append((pivots[-1][0] + i * count, pivots[-1][1] + j * count))

# Perimeter
total = perimeter // 2 + 1
# Inner area size
total += shoelace_area([i for (i, j) in pivots], [j for (i, j) in pivots])

print(total)