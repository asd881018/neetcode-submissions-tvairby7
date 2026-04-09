class letterNode():

    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = letterNode()        

    def addWord(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = letterNode()    
            cur = cur.children[c]
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        
        def dfs(j, root):
            cur = root

            for i in range(j, len(word)):

                c = word[i]

                if c == ".":
                    for child in cur.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:

                    if c not in cur.children:
                        return False
                    # if c is '.', then cur = cur.children[c] is not valid
                    cur = cur.children[c]
            return cur.endOfWord

        return dfs(0, self.root)
