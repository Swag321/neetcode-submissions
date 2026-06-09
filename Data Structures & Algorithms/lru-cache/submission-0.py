class Node:
    def __init__(self, key, val):
        self.left = None
        self.right = None
        self.key = key
        self.val = val

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.cap = capacity
        self.lmost = Node(-1,-1) #dummy leftmost node
        self.rmost = Node(-1,-1) #dummy rightmost node
        self.lmost.right = self.rmost # link them
        self.rmost.left = self.lmost 

    def _getNode(self, key) -> Node:
        output = self.cache.get(key, Node(-1,-1))
        if output.key == -1:
            return output # return flag node if not found
        else:
            #remove and reinsert
            #1. removed
            output.left.right = output.right
            output.right.left = output.left
            #2. reinsert
            output.left = self.rmost.left
            self.rmost.left = output
            output.right = self.rmost # make sure to link
            output.left.right = output 
        
        return output


    def get(self, key: int) -> int:
        """
        1. retrieve node from cache (or Node(-1,-1) if DNE), (make getNode() -> Node)
        1.1. remove this node (change its l,r pointers), 
        1.2. reinsert at rmost.left (1.1 and 1.2 in getNode())
        4. return val
        """
        return self._getNode(key).val

    def put(self, key: int, value: int) -> None:
        """
        1. retrieve node from cache (utilize getNode() -> node) -> val
        2. if (-1,-1) (DNE), insert Node(key,value) at rmost.left
        3. else: update node.val = value
        4. if len(cache) > self.cap: self.lmost.right = self.lmost.right.right
        """
        node = self._getNode(key)
        if node.key == -1:
            # DNE yet; insert at end
            newNode = Node(key,value)
            prev = self.rmost.left
            prev.right = newNode        
            newNode.left = prev         
            newNode.right = self.rmost  
            self.rmost.left = newNode
            self.cache[key] = newNode
        else:
            # val already exists, just update it
            node.val = value
            #don't need to remove/reinsert because getNode() already took care of that.
        
        if len(self.cache) > self.cap:
            lruKey = self.lmost.right.key
            # remove lru node:
            self.lmost.right = self.lmost.right.right
            # relink new lru node to lmost dummy
            self.lmost.right.left = self.lmost 
            # remove cache corresponding to key
            del self.cache[lruKey]
        


