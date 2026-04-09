class Node:
    def __init__(self, key: int, val: int):
        self.key, self.val = key, val
        self.prev, self.next = None, None

class LRUCache:

    def __init__(self, capacity: int):
        # has capacity
        self.cap = capacity
        # hashmap to store the key node position
        self.cache = {}
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    def remove(self, node: Node) -> None:
        # prev <-> node <-> next
        # prev <-> next
        # unlink the prev.next, next.prev from the node
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev
        

    def insert(self, node: Node) -> None:
        # prev = MRU = right.prev
        # next = right
        prev, next = self.right.prev, self.right
        
        # prev <-> next
        # prev <-> node <-> next
        
        # link the prev.next, next.prev to the node
        prev.next = next.prev = node
        # link node.prev and node.next to prev and next
        node.prev, node.next = prev, next
    
    def get(self, key: int) -> int:
        # O(1) look up to see if key is in hashmap or not
        # {1=2, 2=3}, cap = 2
        # get(1)
        # {2=3, 1=2}
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        # O(1) look up to see if key is in hashmap or not
        # Upsert the key-value pair
        if key in self.cache:
            self.remove(self.cache[key])

        self.cache[key] = Node(key, value) 
        self.insert(self.cache[key])

        # Check if the cur cache is exceed the capacity
        # if yes, remove the least recently used (LRU) key-value pair
        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]

        # Problem: How to define which pair is the LRU?

        # {1=2, 2=3}, cap = 2
        # put(4,5)
        # remove 1=2 (LRU)
        # insert 4=5
        # {2=3, 4=5}
        
