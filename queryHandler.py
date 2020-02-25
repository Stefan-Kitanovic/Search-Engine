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
        sets.append(Set(tree.search(word)[1].keys()))   # Popunjavnje liste setova

    currSet = sets[0]
    if len(words) == 1:
        searchResult = currSet
    for i in range(1, len(words)):
        searchResult = union(currSet, sets[i])          # primena OR operatora nad svim recima
        currSet = sets[i]

    return searchInfo, searchResult


def logicsSearch(words, tree: Trie):
    searchInfo = list()     # lista recnika dokumenata svake reci (u skupu rezultata)
    searchResult = Set()    # set rezultata pretrage (linkova)
    temp = list()           # nefiltrirani searchInfo

    temp.append(tree.search(words[0])[1])      # pretraga prve reci
    temp.append(tree.search(words[2])[1])      # pretraga druge reci

    set1 = Set(temp[0].keys())
    set2 = Set(temp[1].keys())
    if words[1] == 'AND':
        searchResult = intersection(set1, set2)
        for word in temp:                      # Filtriranje temp rezultatima pretrage
            dictt = dict()
            for link in searchResult.elems:
                if link in word.keys():
                    dictt[link] = word[link]
            searchInfo.append(dictt)
    elif words[1] == 'OR':
        searchResult = union(set1, set2)
        searchInfo = temp                      # Nije potrebno filtriranje
    elif words[1] == 'NOT':
        searchResult = difference(set1, set2)
        dictt = dict()
        for link in searchResult.elems:        # Filtriranje temp rezultatima pretrage
            if link in temp[0].keys():
                dictt[link] = temp[0][link]
        searchInfo.append(dictt)

    return searchInfo, searchResult

