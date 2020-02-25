class TrieNode:
    def __init__(self, char: str):
        self.val = char.lower()     # Sva slova smestamo kao lowercase (Case insensitive stablo)
        self.children = dict()
        self.isWord = False
        self.documents = dict()     # Ovde smestamo parove: [dokument(koji sadrzi rec) - broj ponavljanja reci]


class Trie:
    def __init__(self):
        self.root = TrieNode('_root')

    def insert(self, word: str, path):
        wordL = word.lower()               # Case insensitive algoritam
        curr = self.root
        for letter in wordL:                                # Iteracija kroz unetu rec
            if letter not in curr.children.keys():          # ako slovo ne pripada deci trenutnog noda stabla:
                curr.children[letter] = TrieNode(letter)    #   napravi novi nod
            curr = curr.children[letter]                    # Prelazak na sledece slovo reci
        curr.isWord = True                                  # Kada zavrsimo ubacivanje oznaci kao postojeca rec
        if path in curr.documents.keys():                   # Proveravamo postojanje putanje u reci kako bi:
            curr.documents[path] += 1                       #   Povecali brojac, ako vec postoji
        else:
            curr.documents[path] = 1                        #   Inicijalizovali brojac/putanju za rec, ako ne postoji

    def search(self, word: str):        # Vraca informaciju da li rec postoji:
        wordL = word.lower()            # ako postoji Vraca: (True, dokumente u kojima je sadrzana i br ponavljanja)
        curr = self.root                # ako ne postoji Vraca: False, {nema rezultata : 0}
        for letter in wordL:            # Radi na istom princpu kao insert
            if letter not in curr.children.keys():
                return False, {'Nema rezultata': 0}
            curr = curr.children[letter]
        if curr.isWord:                 # Ukoliko algoritam pronadje sve grane, ali krajnji node nije rec
            return True, curr.documents
        else:
            return False, {'Nema rezultata': 0}


def trieHTML(words):
    tree = Trie()
    for link in words.keys():                  # iteracija kroz linkove
        for word in words[link]:               # iteracija kroz reci pojedinacnog linka
            tree.insert(word, link)

    return tree
