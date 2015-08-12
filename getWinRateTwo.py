#def get_win_rate_two(patch, champId):
winRates = []
patch = "5.7.0.275"
champId1 = 1
champId2 = 2
with open("{}/winRates.txt".format(patch)) as f:
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
win = 0
play = 0
i = 0
j = 0
while i < len(winRates):
    if j == 5:
        j = 0
        i += 1
    else:
        if winRates[i][0][j] == champId1:
            #check for next champ
            k = j + 1
            while k < 5:
                if winRates[i][0][k] == champId2:
                    win += winRates[i][1]
                    play += winRates[i][2]
                    break
                elif winRates[i][0][k] > champId2:
                    break
                elif winRates[i][0][k] < champId2:
                    k += 1
            j = 0
            i += 1
        elif winRates[i][0][j] > champId1:
            if j == 0:
                break;
            j = 0
            i += 1
        elif winRates[i][0][j] < champId1:
            j += 1
#return [win, play]
