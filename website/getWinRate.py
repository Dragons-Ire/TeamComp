def get_win_rate_champs(patch, champIds):
    winRates = []
    with open("data/{}/winRates.txt".format(patch)) as f:
        for line in f:
            team = []
            line = line.split(',')
            for i in range(len(line)):
                if i < 5:
                    team.append(int(line[i]))
                elif i == 5:
                    wins = int(line[i])
                elif i == 6:
                    plays = int(line[i])
                    break
            winRates.append([team, wins, plays])
    if len(champIds) > 0:
        i = 0
        j = 0
        x = 0
        relevant = []
        while i < len(winRates):
            if j == 5:
                j = 0
                x = 0
                i += 1
            else:
                if winRates[i][0][j] == champIds[x]:
                    if x == len(champIds) - 1:
                        #add to rates
                        relevant.append(winRates[i])
                        j = 0
                        x = 0
                        i += 1
                    else:
                        j += 1
                        x += 1
                elif winRates[i][0][j] > champIds[x]:
                    if j == 0:
                        break;
                    j = 0
                    x = 0
                    i += 1
                elif winRates[i][0][j] < champIds[x]:
                    j += 1
    else:
        relevant = winRates
    maximum = 0
    wins = 0
    plays = 0
    for i in range(len(relevant)):
        wins = wins + relevant[i][1]
        plays = plays + relevant[i][2]
        if relevant[i][1]/relevant[i][2] > relevant[maximum][1]/relevant[maximum][2]:
            maximum = i
        elif relevant[i][1]/relevant[i][2] == relevant[maximum][1]/relevant[maximum][2]:
            if relevant[i][2] > relevant[maximum][2]:
                maximum = i
    if len(relevant) > 0:
        return [wins, plays, relevant[maximum]]
    else:
        return [wins, plays, []]
