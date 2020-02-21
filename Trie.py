import os


class TrieNode:
    def __init__(self, char: str):
        self.val = char.lower()     # Sva slova smestamo kao lowercase (Case insensitive stablo)
        self.children = dict()
        self.isWord = False
        self.documents = dict()     # Ovde smestamo parove: [dokument(koji sadrzi rec) - broj ponavljanja reci]


class Trie:
    def __init__(self):
        self.root = TrieNode('_root')

    def insert(self, word: str):
        wordL = word.lower()
        curr = self.root
        for letter in wordL:
            if letter not in curr.children.keys():
                curr.children[letter] = TrieNode(letter)
            curr = curr.children[letter]
        curr.isWord = True

    def search(self, word: str):
        wordL = word.lower()
        curr = self.root
        for letter in wordL:
            if letter not in curr.children.keys():
                return False
            if letter == word[-1]:
                break
            curr = curr.children[letter]
        return curr.isWord

    def addDocInfo(self, path, word):           # Ubacuje informaciju u documents polje
        wordL = word.lower()                    # Postoji i zastita od unosa u nepostojecu rec
        curr = self.root                        # iako to ne bi trebalo da se desi
        for letter in wordL:
            if letter not in curr.children.keys():
                return False
            curr = curr.children[letter]
        if curr.isWord:
            if path in curr.documents.keys():
                curr.documents[path] += 1
            else:
                curr.documents[path] = 1


def trieHTML(path, parser):
    tree = Trie()
    for root, dirs, files in os.walk(path):
        for file in files:                              # iteracija ide kroz fajlove putanje
            currPath = os.path.join(root, file)         # Postavljamo trenutnu putanju
            if os.path.isfile(currPath) and file.endswith('.html'):  # Ako se fajl zavrsava sa .html parsiraj
                p = parser.parse(currPath)
                for word in p[1]:
                    if not tree.search(word):           # Potrebna optimizacija
                        tree.insert(word)
                    tree.addDocInfo(currPath, word)
    return tree
