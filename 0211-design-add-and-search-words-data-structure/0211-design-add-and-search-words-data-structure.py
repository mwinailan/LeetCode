class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word: str) -> None:
        current = self.root
        for letter in word:
            if letter not in current.children:
                current.children[letter] = TrieNode()
            current = current.children[letter]
        current.endOfWord = True

    def search(self, word: str) -> bool:
        
        def wordSearch(i, node):
            current = node
            for j in range(i, len(word)):
                if word[j] == ".":
                    for child in current.children.values():
                        if wordSearch(j + 1, child):
                            return True
                    return False
                else:
                    if word[j] not in current.children:
                        return False
                    current = current.children[word[j]]
            return current.endOfWord
        
        return wordSearch(0, self.root)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)