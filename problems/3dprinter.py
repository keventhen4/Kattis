"""(Correct 33/33) Sol 1 0.04s Diff:2.7"""
def calculate(input):
    import math
    numStats = input
    return math.ceil(math.log(numStats, 2)) + 1


print(calculate(input()))