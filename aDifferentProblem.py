
"""(Kattis-Unapproved 3/3) Sol #2"""
input = "./input.txt"

with open(input,'r') as f:
    lines = f.readlines()
    for line in lines:
        numbers = line.split()
        print(abs(int(numbers[0]) - int(numbers[-1])))


"""(Correct 3/3) Sol #3"""
import sys

for line in sys.stdin:
    a, b = map(int, line.split())
    print(abs(a - b))


"""(Kattis-Unapproved 3/3) Sol #1 (Mine)"""
def add(input):
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
                yield abs(int(nums[1])-int(nums[2]))
        else:
            if input[charcPos] == ' ':
                numTwo = True
            else:
                yield abs(int(nums[1])-int(nums[2]))
                nums[1] = nums[2] = ''
                numTwo = False


# for value in add("""10 12
# 71293781758123 72784
# 1 12345677654321"""):
#     print(value)


#input = input()

#input = """10 12
#71293781758123 72784
#1 12345677654321"""