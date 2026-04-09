class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} # map key to node

        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left

    # remove node from list
    def remove(self, node):
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev
    
    # insert node at right
    def insert(self, node):
        mru = self.right.prev

        mru.next = self.right.prev = node
        node.next, node.prev = self.right, mru
        

    def get(self, key: int) -> int:
        if key in self.cache:
            # update to most recent
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            # remove and delete the LRU
            lru = self.left.next
            
            self.remove(lru)
            del self.cache[lru.key]
            
        
