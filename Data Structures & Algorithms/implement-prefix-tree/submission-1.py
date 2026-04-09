class PrefixTree:

    def __init__(self):
        self.wordSet = set()

    def insert(self, word: str) -> None:
        self.wordSet.add(word)

    def search(self, word: str) -> bool:
        return word in self.wordSet

    def startsWith(self, prefix: str) -> bool:
        # Itr all the word in wordSet
        # for loop, itr each char in prefix and word to compare
        
        for word in self.wordSet:
            targetLen = 0
            if len(word) < len(prefix):
                continue
            for i in range(len(prefix)):
                if prefix[i] == word[i]:
                    targetLen += 1
                if targetLen == len(prefix):
                    return True
        
        return False