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

    def search(self, word: str):        # Vraca informaciju da li rec postoji:
        wordL = word.lower()            # ako postoji Vraca: (True, dokumente u kojima je sadrzana i br ponavljanja)
        curr = self.root                # ako ne postoji Vraca: False, {nema rezultata : 0}
        for letter in wordL:
            if letter not in curr.children.keys():
                return False, {'Nema rezultata': 0}
            curr = curr.children[letter]
        if curr.isWord:                 # Treba ukoliko algoritam pronadje sve grane, ali krajnji node nije rec
            return True, curr.documents
        else:
            return False, {'Nema rezultata': 0}

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


def trieHTML(words):
    tree = Trie()
    for link in words.keys():                  # iteracija kroz linkove
        for word in words[link]:               # iteracija kroz reci pojedinacnog linka
            if not tree.search(word)[0]:       # Optimizacija ?
                tree.insert(word)
            tree.addDocInfo(link, word)

    return tree
