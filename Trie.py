
class TrieNode:
    def __init__(self, char):
        self.val = char
        self.children = dict()
        self.isWord = False


class Trie:
    def __init__(self):
        self.root = TrieNode('_root')

    def insert(self, word):
        curr = self.root
        letter = ''
        for letter in word:
            if letter not in curr.children.keys():
                curr.children[letter] = TrieNode(letter)
            curr = curr.children[letter]
        curr.isWord = True

    def search(self, word):
        curr = self.root
        for letter in word:
            if letter not in curr.children.keys():
                return False
            curr = curr.children[letter]
        if curr.isWord:
            return True



