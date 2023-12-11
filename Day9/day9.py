IS_PART2 = True

data = []
for line in open("input", "r").read().splitlines():
    data.append(list(map(int, line.split(" "))))


def predict_next_value(mlist):
    reconstructed = mlist.copy()
    storage = [mlist.copy()]
    while any(map(lambda x: x != 0, reconstructed)):
        reconstructed = [reconstructed[i + 1] - reconstructed[i] for i in range(len(reconstructed) - 1)]
        storage.append(reconstructed)
    mres = 0
    if IS_PART2:
        for last in reversed(storage):
            mres = last[0] - mres
    else:
        for last in reversed(storage):
            mres += last[-1]
    return mres


res = 0
for value in data:
    res += predict_next_value(value)

print(res)
