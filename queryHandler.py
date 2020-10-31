from Trie import Trie
from Set import Set


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
        if res[1] == 'NOT' and res[0].lower() == res[2].lower():
            print("Upit nema smisla")
            return
        return res


def standardSearch(words, tree: Trie):
    searchInfo = list()     # lista recnika dokumenata svake reci (u skupu rezultata)
    searchResult = Set()    # set rezultata pretrage (linkova)
    sets = list()           # list setova svake pojedinacne reci

    for word in words:                                  # iteracija kroz reci pretrage
        searchInfo.append(tree.search(word)[1])
        sets.append(Set(list(tree.search(word)[1].keys())))   # Popunjavnje liste setova

    currSet = sets[0]
    if len(words) == 1:
        searchResult = currSet
    for i in range(1, len(words)):
        searchResult = currSet.union(sets[i])          # primena OR operatora nad setovima svih reci (unija)
        currSet = searchResult

    return searchInfo, searchResult


def logicsSearch(words, tree: Trie):
    searchInfo = list()     # lista recnika dokumenata svake reci (u skupu rezultata)
    searchResult = Set()    # set rezultata pretrage (linkova)

    searchInfo.append(tree.search(words[0])[1])      # pretraga prve reci
    searchInfo.append(tree.search(words[2])[1])      # pretraga druge reci

    set1 = Set(list(searchInfo[0].keys()))
    set2 = Set(list(searchInfo[1].keys()))
    if words[1] == 'AND':
        searchResult = set1.intersection(set2)
    elif words[1] == 'OR':
        searchResult = set1.union(set2)
    elif words[1] == 'NOT':
        searchResult = set1.difference(set2)
        searchInfo.pop()

    return searchInfo, searchResult

