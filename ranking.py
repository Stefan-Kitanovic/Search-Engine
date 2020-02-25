def pageRank(graph, pagesToRank, wordCountDict):
    rankedPages = {}
    damping = 0.85

    #Initial ranking (1/N)
    for page in graph.vertices():
        rankedPages[page] = 1/len(graph.vertices())

    avg_change = 1
    while avg_change > 0.00001:
        changes = []
        prevIterationResults = rankedPages

        for page in rankedPages.keys():
            startingRank = rankedPages[page]
            result = 0

            for key in graph.vertices():
                for link in graph.graph[key]:
                    if page == link:
                        result += prevIterationResults[key] / len(graph.graph[key])

            rankedPages[page] = (1-damping)/len(rankedPages.keys()) + damping * result
            endingRank = rankedPages[page]
            changes.append(endingRank - startingRank)

        avg_change = sum(changes) / len(changes) #Average change of ranking per iteration

    rankedResults = {}
    for page in pagesToRank.elems:
        rankedResults[page] = 0

    for page in rankedResults.keys():
        for elem in wordCountDict:
            rankedResults[page] += elem.get(page, 0.5)

    for page in rankedResults.keys():
        for key in graph.vertices():
            for link in graph.graph[key]:
                if page == link:
                    for elem in wordCountDict:
                        rankedResults[page] += elem.get(key, 0.5) * rankedPages[key]

    for page in rankedResults.keys():
        rankedResults[page] += rankedPages[page]

    sortedList = list(rankedResults.keys())

    for i in range(0, len(sortedList)):
        for j in range(0, len(sortedList)):
            if rankedResults[sortedList[i]] > rankedResults[sortedList[j]]:
                sortedList[i], sortedList[j] = sortedList[j], sortedList[i]

    return rankedResults, sortedList