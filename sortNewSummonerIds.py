def merge(left, right):
    result = []
    while (not len(left) == 0) and (not len(right) == 0):
        if left[0] < right[0]:
            result.append(left[0])
            left = left[1:]
        elif left[0] == right[0]:
            left = left[1:]
        else:
            result.append(right[0])
            right = right[1:]
            
    while not len(left) == 0:
        result.append(left[0])
        left = left[1:]
    while not len(right) == 0:
        result.append(right[0])
        right = right[1:]

    return result

def merge_sort(m):
    if len(m) <= 1:
        return m

    mid = len(m) // 2
    left = m[:mid]
    right = m[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)
        

def sort_new_summoner_ids():
    f = open('summonerIds.txt', 'r')
    summonerIds = []
    for summonerId in f:
        summonerIds.append(int(summonerId))
    f.close()
    f = open('newSummonerIds.txt', 'r')
    for summonerId in f:
        summonerIds.append(int(summonerId))
    f.close()
    
    sortedIds = merge_sort(summonerIds)
    
    f = open('summonerIds.txt', 'w')
    for summonerId in sortedIds:
        f.write(repr(summonerId) + '\n')
    f.close()
