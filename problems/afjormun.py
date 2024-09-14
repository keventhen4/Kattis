"""(Correct 31/31) Sol #1 0.07s Diff:1.4-1.6"""

import sys
for line in sys.stdin:
    try:
        int(line)
    except:
        print(line[0].upper()+line[1:len(line)].lower())