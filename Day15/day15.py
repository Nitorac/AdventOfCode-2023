from functools import reduce

data = open('input', 'r').read().replace('\n', '').replace('\r', '').split(',')
print(data)


def hash(input):
    return reduce(lambda old, cur: ((old + (ord(cur))) * 17) % 256, [c for c in input], 0)


total = 0
for item in data:
    total += hash(item)

print(total)
