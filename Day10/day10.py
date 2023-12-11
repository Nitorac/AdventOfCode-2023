IS_PART2 = True

parsed = []
data = {}

for line in open('input', 'r').read().splitlines():
    parsed.append([c for c in line])

# (i1, j1), (i2, j2)
maps = {
    '-': {(0, -1), (0, 1)},
    '|': {(-1, 0), (1, 0)},
    '7': {(1, 0), (0, -1)},
    'F': {(1, 0), (0, 1)},
    'L': {(-1, 0), (0, 1)},
    'J': {(-1, 0), (0, -1)},
}

S = (-1, -1)

for i, line in enumerate(open('input', 'r').read().splitlines()):
    for j, char in enumerate(line):
        if char not in maps:
            if char == 'S':
                S = (i, j)
            continue
        diff1, diff2 = maps[char]
        data[(i, j)] = {
            (i + diff1[0], j + diff1[1]),
            (i + diff2[0], j + diff2[1])
        }

data[S] = set([])
# Find next nodes from S
for k, v in data.items():
    if S in v:
        data[S].add(k)

current = data[S].copy().pop()
last = S
loop = [last, current]
while True:
    old = current
    current = data[current].difference({last}).pop()
    last = old
    loop.append(current)
    if current == S:
        break

if not IS_PART2:
    print(len(loop) // 2)
    exit(0)

maxi, maxj = (max(i for i, j in data.keys()), max(j for i, j in data.keys()))
inside = set([])
for i in range(maxi):
    pipe = 0
    for j in range(maxj):
        current = (i, j)
        if current in loop:
            pipe += 1 if (i - 1, j) in data[current] else 0
        elif pipe % 2 == 1:
            inside.add(current)

print(len(inside))