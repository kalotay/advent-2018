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

def commonletters(ids):
    ids_list = list(ids)
    for index, id in enumerate(ids_list):
        for other in ids_list[index:]:
            common = []
            mismatches = 0
            for left, right in zip(id, other):
                if left == right:
                    common.append(left)
                else:
                    mismatches += 1
                if mismatches > 1:
                    break
            if mismatches == 1:
                return ''.join(common)
    return None

def solve1(filename):
    with open(filename) as f:
        return checksum(f)

def solve2(filename):
    with open(filename) as f:
        return commonletters(f)