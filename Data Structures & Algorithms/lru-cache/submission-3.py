class Node:
    def __init__(self, key: int, val: int):
        self.key, self.val = key, val
        # link
        self.prev, self.next = None, None 

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        # To store key-value, using haspmap, O(1) lookup for the key
        self.cache = {}
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left
        
        # How to identify LRU
        # {1=10}
        # {1=10, 2=8}
        # get(1)
        # {2=8, 1=10}
        # using another hashmap to store the location of the key-value pair

        # left -> Node(1,10) -> Node(2,8) -> right

        # remove Node(1,10)
        # insert Node(1,10) before right

        # left <-> Node(2,8) <-> Node(1,10) <-> right
        # LRU = left.next
        # MRU = right.prev

    def remove(self, node: Node) -> None:
        # prev <-> node <-> next
        # prev <-> next
        # change prev.next and next.prev
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev


    def insert(self, node: Node) -> None:
        # prev <-> next
        # prev <-> node <-> next
        
        # finding prev = MRU = right.prev
        # next = right
        prev, next = self.right.prev, self.right

        # change prev.next and next.prev
        prev.next = next.prev = node
        # change node.prev and node.next
        node.prev, node.next = prev, next


    def get(self, key: int) -> int:
        if key in self.cache:
            # update the location of the node
            node = self.cache[key]
            self.remove(node)
            self.insert(node)

            return node.val
        
        return -1

    def put(self, key: int, value: int) -> None:
        # update/insert the node with new value
        # doesn't matter the key is in cache or not, we need insert
        # but need to remove from the cache first if it is there
        if key in self.cache:
            self.remove(self.cache[key])
        
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        # we are adding new pairs, need to check cap
        if len(self.cache) > self.cap:
            # remove node
            lru = self.left.next
            self.remove(lru)
            # remove cache
            del self.cache[lru.key]

        
