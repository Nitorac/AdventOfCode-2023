IS_PART2 = True

nums = {
    "zero": "z0o",
    "one": "o1e",
    "two": "t2o",
    "three": "t3e",
    "four": "f4r",
    "five": "f5e",
    "six": "s6x",
    "seven": "s7n",
    "eight": "e8t",
    "nine": "n9e"
}

res = 0
for line in open("input", "r").readlines():
    if IS_PART2:
        for k, v in nums.items():
            line = line.replace(k, str(v))
    for c in line:
        if c.isdigit():
            print(c)
            res += 10 * int(c)
            break
    for c in line[::-1]:
        if c.isdigit():
            print(c)
            res += int(c)
            break

print(res)
