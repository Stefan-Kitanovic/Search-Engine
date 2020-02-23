from Trie import Trie
from set import Set, intersection, union, difference

def standardQuery(query: str):
    return query.split(' ')


logOP = ["AND", "OR", "NOT"]


def logicQuery(query: str):
    res = query.split(' ')

    if len(res) != 3 or \
        res[0].upper() in logOP or \
        res[2].upper() in logOP or \
        res[1].upper() not in logOP:
        print("Greska pri unosu!")
        return
    else:
        res[1] = res[1].upper()
        return res


def standardSearch(words, tree: Trie):
    searchInfo = list()     # lista recnika svake reci
    searchResult = Set()
    sets = list()
    n = 0

    for word in words:
        searchInfo.append(tree.search(word)[1])
        sets.append(tree.search(word)[1].keys())

    currSet = sets[-1]
    for i in range(n - 1, -1, -1):
        searchResult = union(currSet, sets[n])

    return searchInfo, searchResult

def logicsSearch(words, tree: Trie):
    searchInfo = list()     # lista recnika svake reci
    searchResult = Set()    # set rezultata pretrage

    searchInfo.append(tree.search(words[0])[1])     # pretraga prve reci
    searchInfo.append(tree.search(words[2])[1])     # pretraga druge reci

    set1 = Set(searchInfo[0].keys())
    set2 = Set(searchInfo[1].keys())
    if words[1] == 'AND':
        searchResult = intersection(set1, set2)
    elif words[1] == 'OR':
        searchResult = union(set1, set2)
    elif words[1] == 'NOT':
        searchResult = difference(set1, set2)

    return searchInfo, searchResult

