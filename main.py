import os

from Trie import Trie, trieHTML
from htmlParser import Parser
import time


def main():
    parser = Parser()
    parsiraniFajlovi = list()
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
                print("\nUneti direktorijum ne postoji!\n")
                continue

            t1 = time.time()
            trieTree = trieHTML(path, parser)
            t2 = time.time()
            print('Vreme izgradnje trie stabla: ' + str(t2 - t1))

        elif opt == "2":
            pass
        elif opt == "3":
            pass
        elif opt == "4":
            pass
        elif opt == "0":
            return


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
