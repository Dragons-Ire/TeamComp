import json

def get_winners_losers(patch):
    winners = []
    losers = []

    for i in range(1, 2151):
        with open('{}/match{}.json'.format(patch,i)) as matchSet:
            matches = json.load(matchSet)
        for match in matches["matches"]:
            team1 = []
            team2 = []
            for participant in match["participants"]:
                if participant["teamId"] == 100:
                    team1.append(participant["championId"])
                else:
                    team2.append(participant["championId"])
            team1.sort()
            team2.sort()
            if match["teams"][0]["winner"] == True:
                winners.append(team1)
                losers.append(team2)
            else:
                winners.append(team2)
                losers.append(team1)
        print("Set " + repr(i) + " Added")
    winners.sort()
    losers.sort()
    f = open("{}/winners.txt".format(patch), 'w')
    for team in winners:
        for champ in team:
            f.write(repr(champ) + ',')
        f.write('\n')
    f.close()
    f = open("{}/losers.txt".format(patch), 'w')
    for team in losers:
        for champ in team:
            f.write(repr(champ) + ',')
        f.write('\n')
    f.close()
