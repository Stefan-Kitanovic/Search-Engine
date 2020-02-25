def pageRank(filesForSorting, wordCountDict, graph):
    rankedResults = {}
    damping = 0.85

    #Initial ranking (1/N)
    for page in graph.vertices():
        rankedResults[page] = 1/len(graph.vertices())

    avg_change = 1
    while avg_change > 0.00001:
        changes = []
        prevIterationResults = rankedResults

        for page in rankedResults.keys():
            startingRank = rankedResults[page]
            result = 0

            for key in graph.vertices():
                for link in graph.graph[key]:
                    if page == link:
                        result += prevIterationResults[key] / len(graph.graph[key])

            rankedResults[page] = (1-damping) + damping * result
            endingRank = rankedResults[page]
            changes.append(endingRank - startingRank)

        avg_change = sum(changes) / len(changes) #Average change of ranking per iteration

    for page in rankedResults.keys():
        rankedResults[page] /= len(rankedResults.keys())


    sortedList = list(rankedResults.keys())

    for i in range(0, len(sortedList)):
        for j in range(0, len(sortedList)):
            if rankedResults[sortedList[i]] > rankedResults[sortedList[j]]:
                sortedList[i], sortedList[j] = sortedList[j], sortedList[i]

    return rankedResults, sortedList