"""(Correct 59/59) Sol #1 0.04s Diff:1.6"""

import sys
for line in sys.stdin:
    hrs = int(line)//(60**2)
    mins = (int(line)//60)%60
    sec = int(line)%60
    print(hrs," : ",mins," : ",sec)