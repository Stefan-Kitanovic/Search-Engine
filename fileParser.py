import os


def parseFiles(path, parser):
    edges = []
    words = []

    for root, dirs, files in os.walk(path):
        for file in files:  # iteracija ide kroz fajlove putanje
            currPath = os.path.join(root, file)  # Postavljamo trenutnu putanju
            if os.path.isfile(currPath) and file.endswith('.html'):  # Ako se fajl zavrsava sa .html parsiraj
                p = parser.parse(currPath)

                for link in p[0]:
                    edges.append([currPath, link])

                for word in p[1]:
                    words.append(word)
    return edges, words