class ListNode:
    def __init__(self, key = 0, val = 0):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.left = ListNode()
        self.right = ListNode()
        self.left.next = self.right
        self.right.prev = self.left
        self.capacity = capacity
        self.cache = {}
    
    def remove(self, node: ListNode):
        node.prev.next = node.next
        node.next.prev = node.prev
        del node
    
    def add(self, node: ListNode):
        node.next = self.right
        node.prev = self.right.prev
        self.right.prev.next = node
        self.right.prev = node

    def get(self, key: int) -> int:
        val = -1
        if key in self.cache:
            val = self.cache[key].val
            self.remove(self.cache[key])
            self.cache[key] = ListNode(key, val)
            self.add(self.cache[key])
        return val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            val = self.cache[key].val
            self.remove(self.cache[key])
        self.cache[key] = ListNode(key, value)
        self.add(self.cache[key])

        print(self.cache)
        if len(self.cache) > self.capacity:
            oldNode = self.left.next
            self.cache.pop(oldNode.key)
            self.remove(oldNode)

        
