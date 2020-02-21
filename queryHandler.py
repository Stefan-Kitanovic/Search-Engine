
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
