import os


def parseFiles(path, parser):
    edges = []
    words = {}  # {link: reci_na_linku}

    for root, dirs, files in os.walk(path):
        for file in files:  # iteracija ide kroz fajlove putanje
            currPath = os.path.join(root, file)  # Postavljamo trenutnu putanju
            if os.path.isfile(currPath) and file.endswith('.html'):  # Ako se fajl zavrsava sa .html parsiraj
                p = parser.parse(currPath)

                for link in p[0]:
                    edges.append([currPath, link])

                words[currPath] = p[1]
    return edges, words