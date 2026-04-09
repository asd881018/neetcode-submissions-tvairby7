class Node:
    def __init__(self, key: int, val:int):
        self.key, self.val = key, val
        self.prev, self.next = None, None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        # use a hashmap to store the key-value pair
        self.cache = {}
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

        # How to identify Least Recently Used (LRU)
        # Node
        # Hasmap store the key-node
        # left <-> LRU <-> 1:2 <-> 2:3 <-> MRU <-> right
        # LRU = left.next
        # MRU = right.prev

    def remove(self, node: Node) -> None:
        # prev <-> node <-> next
        # prev <-> next
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev
    
    def insert(self, node: Node) -> None:
        # prev <-> next
        # prev <-> node <-> next
        prev, next = self.right.prev, self.right
        prev.next = next.prev = node
        node.prev, node.next = prev, next
        
    
    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            # Move the node as MRU
            self.remove(node)
            self.insert(node)
            return node.val
        return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        # if exceed the capacity
        if len(self.cache) > self.cap:
            # remove LRU node and its key-node pair in cache
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]

        
