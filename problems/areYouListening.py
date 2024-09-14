"""(Correct 30/30) Sol #1 0.04s Diff:2.5"""

import sys, math

posn, dists = [], []

def distant(posr):
    distance = math.sqrt((posr[0] - posn[0])**2 + (posr[1] - posn[1])**2)
    return 0 if distance <= posr[2] else distance-posr[2]

for line in sys.stdin:
    if posn:
        if len(dists) < posn[2]:
            dists.append(distant([int(i) for i in line.split()]))
        if len(dists) == posn[2]:
            dists = [math.floor(i) for i in sorted(dists)[:3]]
            print( min(dists) if dists[0] == dists[2] else max(dists) )
    posn = [int(i) for i in line.split()] if not posn else posn