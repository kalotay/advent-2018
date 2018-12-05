from collections import namedtuple
import re

DAY = 3

CLAIM_PATTERN = re.compile(r'#(?P<id>\S+)\s+@\s+(?P<left>\d+),(?P<top>\d+):\s+(?P<width>\d+)x(?P<height>\d+)')

def overlaparea(claims):
    claims_iter = (parseclaim(c) for c in claims)
    calculator = OverlapCalculator()
    for claim in claims_iter:
        calculator.addclaim(claim)
    return calculator.overlaparea()

def findunique(claims):
    claims_iter = (parseclaim(c) for c in claims)
    calculator = OverlapCalculator()
    for claim in claims_iter:
        calculator.addclaim(claim)
    return calculator.uniques()


Claim = namedtuple('Claim', ['id', 'left', 'top', 'width', 'height'])

def parseclaim(claim):
    match = CLAIM_PATTERN.match(claim)
    if not match:
        return None
    return Claim(id=match.group('id'), left=int(match.group('left')), top=int(match.group('top')), width=int(match.group('width')), height=int(match.group('height')))

class OverlapCalculator:
    def __init__(self):
        self._claims = []
        self._overlaps = set()
        self._uniques = set()

    def overlaparea(self):
        return len(self._overlaps)

    def uniques(self):
        return self._uniques

    def addclaim(self, claim):
        self._uniques.add(claim.id)
        self._computeoverlaps(claim)
        self._claims.append(claim)

    def _computeoverlaps(self, claim):
        for c in self._claims:
            overlap = _computeoverlap(claim, c)
            count = 0
            for coord in overlap:
                self._overlaps.add(coord)
                count += 1
            if count != 0:
                self._uniques.discard(c.id)
                self._uniques.discard(claim.id)


def _computeoverlap(claim_a, claim_b):
    left_a, right_a, top_a, bottom_a = _corners(claim_a)
    left_b, right_b, top_b, bottom_b = _corners(claim_b)
    left = max(left_a, left_b)
    right = min(right_a, right_b)
    top = max(top_a, top_b)
    bottom = min(bottom_a, bottom_b)
    x = left
    while x < right:
        y = top
        while y < bottom:
            yield (x, y)
            y += 1
        x += 1

def _corners(claim):
    c = (claim.left, claim.left + claim.width, claim.top, claim.top + claim.height)
    return c

def solve1(filename):
    with open(filename) as f:
        return overlaparea(f)

def solve2(filename):
    with open(filename) as f:
        return findunique(f)
