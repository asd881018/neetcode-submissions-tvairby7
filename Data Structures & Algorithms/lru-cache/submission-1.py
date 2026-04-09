class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:

    # left -> LRU -> ... -> MRU -> right
    # left and right are dummy nodes, we just want
    # LRU = left.next
    # MRU = right.prev

    # using hashmap for cache, to store key-value
        # Problem: how to find the Least Recent Used (LRU)
        # {1-Node(1,3), 2-Node(2,4)}
        # if we need to update key=1's value = 5
        # remove it
        # {2-Node(2,4)}
        # insert
        # {2-Node(2,4), 1-Node(1,3)}
        # key-pointer

        # if len(cache) > cap:
        # remove the 1st element in the cache

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} # store key-pointer(Node(key, value))
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node: Node) -> None:
        # prev <-> node <-> next
        # prev <-> next

        # change next.prev and prev.next
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev
    
    def insert(self, node: Node) -> None:
        # insert as MRU = right.prev
        # prev <-> next
        # prev <-> node <-> next

        prev, next = self.right.prev, self.right
        prev.next = next.prev = node 
        node.prev, node.next = prev, next
        

    def get(self, key: int) -> int:
        # remove then inserting same key-pointer
        if key in self.cache:
            # update the pointer location
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        
        return -1

    def put(self, key: int, value: int) -> None:
        # remove then inserting same key but new pointer
        # also update the cache if we have exceed the limit
        if key in self.cache:
            # update the pointer location
            self.remove(self.cache[key])
        # insert the new one
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        # if it exceed the capacity, remove the 1st one in node list, and the cache
        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
            

        
