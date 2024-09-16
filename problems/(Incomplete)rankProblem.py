""""""

import sys

teams, games, rankings = 0, 1, []
numgames = 0


for line in sys.stdin:
    if teams and numgames < games:
        winteam, loseteam = int(line.split()[0][1]), int(line.split()[1][1])
        windex, losedex = rankings.index(winteam), rankings.index(loseteam)
        if windex > losedex:
            for i in range(losedex, windex):
                rankings[i] = rankings[i+1]
            rankings[windex] = loseteam
        numgames += 1

    elif games:
        teams = int(line.split()[0])
        games = int(line.split()[1])
        for team in range(teams): rankings.append(team+1)

    if numgames == games:
        for i in range(len(rankings)):
            rankings[i] = "T" + str(rankings[i])
        print(" ".join(rankings))