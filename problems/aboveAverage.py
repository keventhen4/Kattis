"""(Correct 2/2) Sol #1 0.04s Diff:2.0"""

import sys
numTests, aboveAv = 0, []

for line in sys.stdin:
    if numTests:
        data = [int(i) for i in line.split()]
        average = sum(data[1:]) / data[0]
        aboveAv.append(round(len([i for i in data[1:] if i > average]) / data[0] * 100, 3))
    else:
        numTests = int(line)
    
    if len(aboveAv) == numTests:
        for i in aboveAv:
            first = str(i).split('.')[0]
            second = str(i).split('.')[1]
            while len(second) < 3:
                second += '0'
            print(first + '.' + second[:3] + '%')