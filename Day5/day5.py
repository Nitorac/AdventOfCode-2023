lines = [line.rstrip('\n') for line in open("input", "r").readlines()]
starts = list(map(lambda x: int(x), lines[0].split(': ')[1].split(' ')))
ends = []


def parse(file_lines):
    maps = []
    cur_lst = []
    for line in file_lines[3:]:
        line = line.strip()
        if line == '':
            cur_lst.sort()
            maps.append(cur_lst)
            cur_lst = []
        elif not "map" in line:
            read = tuple(map(lambda x: int(x), line.split(' ')))
            cur_lst.append((read[1], read[1] + read[2], read[0] - read[1]))
    if cur_lst:
        cur_lst.sort()
        maps.append(cur_lst)
    return maps

def transform_range_through_map(seed_ranges, mappings):
    for start, end in seed_ranges:
        for start2, end2, offset in mappings:
            if start2 >= end or start >= end2:
                continue
            if start < start2:
                yield start, start2
                start = start2
            end2 = min(end, end2)
            yield start + offset, end2 + offset
            start = end2
        if start < end:
            yield start, end


maps = parse(lines)
stages = [(starts[i], starts[i] + starts[i+1]) for i in range(0, len(starts), 2)]
for mymap in maps:
    stages = transform_range_through_map(stages, mymap)

print(min(stages, key=lambda x: x[0])[0])
