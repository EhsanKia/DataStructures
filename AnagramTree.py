from collections import Counter

class Tree:
    def __init__(self):
        self.words = []
        self.children = {}

    def __repr__(self):
        return "Words:" + ', '.join(self.words)


#alphabet =  "zqxjkvbpygfwmucldrhsnioate"
alphabet =  "jqxzwkvfybhgmpudlotnraise"
#alphabet =  "qjxzwkvfybhgmpudclrtanoise"
#alphabet = "abcdefghijklmnopqrstuvwxyz"

root = Tree()

with open(r"words.txt",'r') as f:
    for line in f:
        word = line.strip('\n')
        h = Counter(word)
        curNode = root

        for s in alphabet:
            f = h[s]
            curNode = curNode.children.setdefault(f,Tree())

        curNode.words.append(word)

def find(letters):
    frontier = [root]
    h = Counter(letters)
    for s in alphabet:
        newFrontier = []
        f = h[s]
        for node in frontier:
            for i in range(f+1):
                if node.children.has_key(i):
                    newFrontier.append(node.children[i])
        frontier = newFrontier
        
    ans = []
    for node in frontier:
        ans.extend(node.words)

    return ans
    
def numnode(node):
    tot = 0
    tot += len(node.children.keys())
    for k in node.children:
        tot += numnode(node.children[k])
    return tot
