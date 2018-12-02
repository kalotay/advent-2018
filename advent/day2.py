from collections import Counter

DAY = 2

def checksum(ids):
    twos = 0
    threes = 0
    for id in ids:
        counts = _getcounts(id)
        if 2 in counts:
            twos += 1
        if 3 in counts:
            threes += 1
    return twos * threes

def _getcounts(id):
    counter = Counter(id)
    return frozenset(counter.values())

def solve1(filename):
    with open(filename) as f:
        return checksum(f)