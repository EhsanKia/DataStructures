import Levenshtein as lv

# Tree holding the dictionary
class Tree:
    def __init__(self, word):
        self.word = word
        self.children = {}

    # Adding a word to the tree
    def add_word(self, word):
        d = lv.distance(self.word, word)
        if d in self.children.keys():
            self.children[d].add_word(word)
        else:
            self.children[d] = Tree(word)

    # Search for a word of distance <= n
    def search(self, word, n):
        res = []
        d = lv.distance(self.word, word)
        if d <= n:
            res.append(self.word)   
        for child in self.children.keys():
            if abs(child - d) <= n:
                res = res + self.children[child].search(word, n)
        return res


# Adds all the words in words.txt to the tree
with open('words.txt', 'r') as f:
    dic = Tree(f.readline().strip('\n'))

    for word in f:
        word = word.strip('\n')
        dic.add_word(word)
