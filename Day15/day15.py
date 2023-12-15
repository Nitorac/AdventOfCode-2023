from functools import reduce

IS_PART2 = True

data = [line.strip() for line in open('input', 'r').read().replace('\n', '').replace('\r', '').split(',')]


def hash(input):
    return reduce(lambda old, cur: ((old + (ord(cur))) * 17) % 256, [c for c in input], 0)


def handle_lens(lens, boxes):
    if lens[-1] == '-':
        key = lens[:-1]
        box = boxes[hash(key)]
        if key in box['order']:
            box['order'].remove(key)
    else:
        key, val = lens.split('=')
        val = int(val)
        box = boxes[hash(key)]
        box['values'][key] = val
        if not key in box['order']:
            box['order'].append(key)


def display_boxes(boxes):
    for i, box in enumerate(boxes):
        if len(box['order']) > 0:
            print(f"[Box {i}] {','.join(map(lambda x: x + '=' + str(box['values'][x]), box['order']))}")


boxes = [{"values": {}, "order": []} for _ in range(256)]

total = 0

for item in data:
    handle_lens(item, boxes)
    if not IS_PART2:
        total += hash(item)

if IS_PART2:
    for i, box in enumerate(boxes):
        for j, lens in enumerate(box['order']):
            total += (i + 1) * (j + 1) * box['values'][lens]

print(total)
