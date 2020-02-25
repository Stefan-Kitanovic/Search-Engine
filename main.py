import os
import time

from Trie import Trie, trieHTML
from htmlParser import Parser
import queryHandler
from graph import Graph
from fileParser import parseFiles
from set import Set

def main():
    parser = Parser()
    parsed = False
    searchInfo = list()       # lista recnika {link: br ponavljanja na linku} za svaku pretrazenu rec
    searchResult = Set()      # lista konacnih rezultata pretrage (linkova)
    trieTree = None
    graph = Graph()
    edges = []
    words = {}
    opt = -1
    while opt:
        print("\nIzabrati opciju: ")
        print("1 - Parsiranje datoteka")
        print("2 - Pretraga")
        print("3 - Prikaz rezultata")
        print("4 - Paginacija")
        print("0 - Izlaz\n")
        opt = input('>> ')

        if opt == "1":
            path = inputDirectory()
            if not os.path.exists(path):
                print("Uneti direktorijum ne postoji!\n")
                continue
            if not os.path.isdir(path):
                print("Uneta putanja nije direktorijum!\n")
                continue

            parsed = False          # Zastita ukoliko dodje do greske tokom parsiranja
            t1 = time.time()
            print("Parsiranje . . .")
            edges, words = parseFiles(path, parser)
            print("Parsiranje uspeno.")
            t2 = time.time()
            print("Izgradnja grafa . . .")
            for edge in edges:
                graph.add_edge(edge)

            print("Izgradnja grafa uspesna.")
            t3 = time.time()
            print("Izgradnja trie stabla . . .")
            trieTree = Trie()
            trieTree = trieHTML(words)
            t4 = time.time()
            print("Izgradnja trie stabla uspesna.")
            print('--> Vreme parsiranja: ' + str(t2 - t1))
            print('--> Vreme izgradnje grafa: ' + str(t3 - t2))
            print('--> Vreme izgradnje trie stabla: ' + str(t4 - t3))
            parsed = True
            del t1, t2, t3, t4, edge, edges, words      # Oslobadjamo memoriju od bespotrebnih promenljivih

        elif opt == "2":
            if not parsed:
                print("Prvo izvrsiti parsiranje!\n")
                continue
            param = -1
            while param:
                print("Izabrati format pretrage:")
                print("1 - Standardna pretraga: [rec1 rec2 rec3 ...]")
                print("2 - Logicka pretraga:    [rec1 OP rec2]  *OP = {AND, OR, NOT}")
                print("0 - Napusti opciju")
                param = input(">> ")
                if param == '0':
                    break
                elif param == '1':
                    query = input("Pretrazi: ")
                    splitted = queryHandler.standardQuery(query)
                    if len(splitted) != 0:
                        searchInfo, searchResult = queryHandler.standardSearch(splitted, trieTree)
                    del query
                    break
                elif param == '2':
                    query = input("Pretrazi: ")
                    splitted = queryHandler.logicQuery(query)
                    if splitted is not None:
                        searchInfo, searchResult = queryHandler.logicsSearch(splitted, trieTree)
                        if splitted[1] == 'NOT':
                            splitted.pop()
                        splitted.pop(1)
                    del query
                    break

        elif opt == "3":                        # Trenutno samo za test prikaz

            print("Pojedinacni rezultati:")
            for i in searchInfo:
                for j in i.keys():
                    print(j, " : ", i[j])
                print("")
            print("Konacni rezultati:")
            for i in searchResult.elems:
                print(i)
        elif opt == "4":
            pass
        elif opt == "0":
            return
        else:
            print("Nepostojeca opcija!\n")


def inputDirectory():
    if input("Nadovezati se na " + os.getcwd() + " (y/n)? ") == 'y':
        path = os.path.abspath(os.getcwd())
        print('-' * 10 + "Trenutni direktorijum:" + '-' * 11)
        print(os.listdir(path))
        print('-' * 45)
        root = input("Uneti root direktorijum za parsiranje ('.' za trenutni): ")
        if root != '.':
            path = os.path.join(path, root)
    else:
        path = input("Uneti root direktorijum za parsiranje: ")

    return path


if __name__ == '__main__':
    main()
