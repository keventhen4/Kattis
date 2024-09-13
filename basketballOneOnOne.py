"""(Correct 16/16) Sol #2"""
def win(input):
    return input[-2]


"""(Correct 16/16) Sol #3"""
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


"""(Incorrect 3/16) Sol (Mine)"""
def Win(input):
    points = [0,0]
    curPla = 0
    tiedToTen = False
    for charcPos in range(1, len(input)+1):
        if (charcPos)%2 != 0:
            curPla = 0 if input[charcPos-1] == "A" else 1
        else:
            points[curPla] += int(input[charcPos-1])
            if points[0] == points[1] == 10:
                tiedToTen = True
    if tiedToTen:
        if abs(points[0]-points[1]) >= 2:
            return "A" if points[0] > points[1] else "B"
    else:
        for plaPos in range(1, len(points)+1):
            if points[plaPos-1] >= 11: return "A"
            if points[plaPos-1] >= 11: return "B"