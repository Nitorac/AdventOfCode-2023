from functools import cache

IS_PART2 = False

data = []

for mline in open('input', 'r').read().splitlines():
    main_split = mline.split(' ')
    data.append({
        "line": main_split[0],
        "groups": list(map(int, main_split[1].split(',')))
    })


@cache
def compute_count(line, groups):
    # If there is no more groups
    if len(groups) == 0:
        # If we found a '#', it's not possible since we don't have any group left in 'groups'!
        # else we have matched all groups until here so this possibility is ok
        return 0 if '#' in line else 1
    # It's not possible to have a match in an empty line or in a group larger than the line
    if not line or groups[0] > len(line):
        return 0
    # If the next token is a '.', we skip it
    if line[0] == '.':
        return compute_count(line[1:], groups)
    # If we found a starting group
    if line[0] == '#':
        # It's not possible to have a '.' in a group so 0 if it is the case
        if '.' not in line[:groups[0]]:
            # else if the rest of the line is the same length as the group (and all the group is not '.')
            if len(line) == groups[0]:
                # It is only possible if there is only 1 group left (the other group could not have a length of 0)
                return 1 if len(groups) == 1 else 0
            # We check that the group is only composed by a number of 'groups[0]' of char '#'
            # (we don't want larger groups than asked)
            if line[groups[0]] != '#':
                # Yay, we have found a full group !
                # We can consume it and parse from the next char after the group in the line
                return compute_count('.' + line[groups[0] + 1:], groups[1:])
        return 0
    # If we have a '?', then we add both possibilities
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