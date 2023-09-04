class TrieNode:
    def __init__(self):
        self.children = {}
        self.isAWord = False
    

class Trie:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        currentNode = self.root
        for letter in word:
            if letter not in currentNode.children:
                currentNode.children[letter] = TrieNode()
            currentNode = currentNode.children[letter]
            
        currentNode.isAWord = True
            
        
        

    def search(self, word: str) -> bool:
        currentNode = self.root
        for letter in word:
            if letter not in currentNode.children:
                return False
            currentNode = currentNode.children[letter]
        
        return currentNode.isAWord

    def startsWith(self, prefix: str) -> bool:
        currentNode = self.root
        for letter in prefix:
            if letter not in currentNode.children:
                return False
            currentNode = currentNode.children[letter]
        
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)