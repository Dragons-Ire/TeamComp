import json
import os, os.path

def get_summoner_ids(patch):
    summonerIds = []
    numberOfMatches = len([x for x in os.listdir("{}/matches/".format(patch)) if os.path.isfile(os.path.join("{}/matches/".format(patch), x))])
    for i in range(1, numberOfMatches):
        with open('{}/matches/match{}.json'.format(patch,i)) as matchSet:
            matches = json.load(matchSet)
        for match in matches['matches']:
            for participant in match['participantIdentities']:
                summonerIds.append(participant['player']['summonerId'])
        print(repr(i + 1) + " match files searched")

    f = open('newSummonerIds.txt', 'w')
    for summonerId in summonerIds:
        f.write(repr(summonerId) + '\n')
    f.close()
