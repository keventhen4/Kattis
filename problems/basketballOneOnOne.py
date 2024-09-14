"""Diff:1.5"""

"""(Correct 16/16) Sol #2 0.04s"""
def win(input):
    return input[-2]


"""(Correct 16/16) Sol #3 0.04s"""
def to_win(a,b):
    if abs(a-b) >= 2:
        if a > 10 or b > 10:
            if a>b:
                return 'A'
            else:
                return 'B'
    return 0

def test(input):
    players = {}
    players['A'] = 0
    players['B'] = 0
    for i in range(0,len(input),2):
        players[input[i]] += int(input[i+1])
        won = to_win(players['A'],players['B'])
        if won!=0:
            return won
print(test("A2B2A1B2A2B1A2B2A1B2A1A1B1A1A2"))