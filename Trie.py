import os


class TrieNode:
    def __init__(self, char: str):
        self.val = char.lower()
        self.children = dict()
        self.isWord = False


class Trie:
    def __init__(self):
        self.root = TrieNode('_root')

    def insert(self, word: str):
        wordL = word.lower()
        curr = self.root
        for letter in word.lower():
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


def trieHTML(path, parser):
    tree = Trie()
    for root, dirs, files in os.walk(path):
        for file in files:                              # iteracija ide kroz fajlove putanje
            currPath = os.path.join(root, file)         # Postavljamo trenutnu putanju
            if os.path.isfile(currPath) and file.endswith('.html'):  # Ako se fajl zavrsava sa .html parsiraj
                p = parser.parse(currPath)
                for word in p[1]:
                    if not tree.search(word):
                        tree.insert(word)
    return tree