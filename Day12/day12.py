from functools import cache

IS_PART2 = True

data = []

for mline in open('input', 'r').read().splitlines():
    main_split = mline.split(' ')
    data.append({
        "line": main_split[0],
        "groups": list(map(int, main_split[1].split(',')))
    })


@cache
def compute_count(line, groups):
    if len(groups) == 0:
        return 0 if '#' in line else 1
    if not line or groups[0] > len(line):
        return 0
    if line[0] == '.':
        return compute_count(line[1:], groups)
    if line[0] == '#':
        if '.' not in line[:groups[0]]:
            if len(line) == groups[0]:
                return 1 if len(groups) == 1 else 0
            if line[groups[0]] != '#':
                return compute_count('.' + line[groups[0] + 1:], groups[1:])
        return 0
    return compute_count('.' + line[1:], groups) + compute_count('#' + line[1:], groups)


total = 0
for play in data:
    mline, mgroups = play['line'], play['groups']
    if IS_PART2:
        mgroups = mgroups * 5
        mline = '?'.join([mline] * 5)
    mysize = compute_count(mline, tuple(mgroups))
    total += mysize

print(total)