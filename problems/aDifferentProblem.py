"""Diff:2.6"""

"""(Correct 3/3) Sol #2"""
import sys

for line in sys.stdin:
    numbers = line.split()
    print(abs(int(numbers[0]) - int(numbers[-1])))


"""(Correct 3/3) Sol #3"""
import sys

for line in sys.stdin:
    a, b = map(int, line.split())
    print(abs(a - b))


"""(Correct 3/3) Sol #1 (Mine)"""
import sys
for line in sys.stdin:
    nums = {}
    nums[1] = nums[2] = ''
    numTwo = False
    for charcPos in range(len(input)):
        if input[charcPos] not in [' ', '\n']:
            if numTwo:
                nums[2] += input[charcPos]
            else:
                nums[1] += input[charcPos]
            if charcPos == len(input)-1:
                print(abs(int(nums[1])-int(nums[2])))
        else:
            if input[charcPos] == ' ':
                numTwo = True
            else:
                print(abs(int(nums[1])-int(nums[2])))
                nums[1] = nums[2] = ''
                numTwo = False