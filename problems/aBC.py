"""(Correct 16/16) Sol #1 0.04s Diff:2.3"""

import sys

nums, order, porder = [], [], ['a', 'b', 'c']

for line in sys.stdin:
    if not nums:
        nums = sorted([int(i) for i in line.split()])
    elif not order:
        order = [porder.index(charc.lower()) for charc in line if charc != "\n"]
    if nums and order:
        print(nums[order[0]],' ',nums[order[1]],' ',nums[order[2]])