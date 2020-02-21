import os
import time

from Trie import Trie, trieHTML
from htmlParser import Parser
import queryHandler


def main():
    parser = Parser()
    parsedFiles = list()
    trieTree = None
    opt = -1
    while opt:
        print("Izabrati opciju: ")
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

            t1 = time.time()
            trieTree = trieHTML(path, parser)
            t2 = time.time()
            print('Vreme izgradnje trie stabla: ' + str(t2 - t1))

        elif opt == "2":
            param = -1
            while param not in range(3):
                print("Izabrati format pretrage:")
                print("1 - Standardna pretraga: [rec1 rec2 rec3 ...]")
                print("2 - Logicka pretraga:    [rec1 OP rec2]  *OP = {AND, OR, NOT}")
                print("0 - napusti opciju")
                param = int(input(">> "))
                if param == 0:
                    continue
                elif param == 1:
                    query = input("Pretrazi: ")
                    splited = queryHandler.standardQuery(query)
                elif param == 2:
                    query = input("Pretrazi: ")
                    splited = queryHandler.logicQuery(query)

        elif opt == "3":
            pass
        elif opt == "4":
            pass
        elif opt == "0":
            return
        else:
            print("Greska pri unosu!\n")


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
