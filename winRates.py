def get_win_rates(patch):
    winners = []
    losers = []
    winRates = []
    with open('{}/winners.txt'.format(patch)) as f:
        for line in f:
            team = []
            line = line[:-2].split(',')
            for char in line:
                team.append(int(char))
            winners.append(team)
    with open('{}/losers.txt'.format(patch)) as f:
        for line in f:
            team = []
            line = line[:-2].split(',')
            for char in line:
                team.append(int(char))
            losers.append(team)
    print("data loaded")
    winRates = []
    for i in range(len(winners)):
        if not winRates == []:
            if winRates[-1][0] == winners[i]:
                winRates[-1][1] += 1
                winRates[-1][2] += 1
            else:
                winRates.append([winners[i], 1, 1])
        else:
            winRates.append([winners[i], 1, 1])
    j = 0
    for i in range(len(losers)):
        k = 0
        while j < len(winRates):
            if winRates[j][0][k] < losers[i][k]:
                j += 1
                k = 0
            elif winRates[j][0][k] == losers[i][k]:
                if k < 4:
                    k += 1
                else:
                    winRates[j][2] += 1
                    break
            else:
                winRates.insert(j, [losers[i], 0, 1])
                break
    print("winRates calculated")
    f = open("{}/winRates.txt".format(patch), 'w')
    for team in winRates:
        for champ in team[0]:
            f.write(repr(champ) + ',')
        f.write(repr(team[1]) + ',' + repr(team[2]) + '\n')
    f.close()
