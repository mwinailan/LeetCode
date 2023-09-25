class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
        
class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {} # (key, node)
        self.capacity = capacity
        self.left = Node(0,0) # least recently used node
        self.right = Node(0,0) # most recently used node
        
        self.left.next, self.right.prev = self.right, self.left
        
    def remove(self, node):
        prevNode, nextNode = node.prev, node.next
        prevNode.next, nextNode.prev = nextNode, prevNode
    
    def insertRight(self, node):
        prevNode, nextNode = self.right.prev, self.right
        prevNode.next, nextNode.prev = node, node
        node.next, node.prev = nextNode, prevNode
        

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insertRight(self.cache[key])
            return self.cache[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
            del self.cache[key]
        
        newNode = Node(key,value)
        self.insertRight(newNode)
        self.cache[key] = newNode
        
        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)