class Map:
    name = "Binary Search Tree"
    def __init__(self, size):
        self.root = None

    def put(self, key, val):
        # Wrapper function
        if self.root:
            self._put(self.root, key, val)
        else:
            self.root = Node()
            self.root.key = key
            self.root.val = val

    def _put(self, node, key, val):
        if key == node.key:
            node.val = val
        elif key > node.key:
            if node.right:
                self._put(node.right, key, val)
            else:
                node.right = Node()
                node.right.key = key
                node.right.val = val
        else:
            if node.left:
                self._put(node.left, key, val)
            else:
                node.left = Node()
                node.left.key = key
                node.left.val = val


    def get(self, key):
        # Wrapper function
        if self.root:
            return self._get(self.root, key)
        else:
            return None
    
    def _get(self, node, key):
        if key == node.key:
            return node.val
        elif key > node.key:
            if node.right:
                return self._get(node.right, key)
            else:
                return None
        else:
            if node.left:
                return self._get(node.left, key)
            else:
                return None


    def delete(self, key):
        # Wrapper function
        self._delete(self.root, key)

    def _delete(self, node, key):
        if node is None: 
            return node
  
        if key < node.key: 
            node.left = self._delete(node.left, key) 

        elif(key > node.key): 
            node.right = self._delete(node.right, key) 
    
        else: 
            if node.left is None: 
                temp = node.right  
                node = None 
                return temp  
                
            elif node.right is None : 
                temp = node.left  
                node = None
                return temp 
     
            temp = self.minValueNode(node.right) 
    
            node.key = temp.key
            node.val = temp.val

            node.right = self._delete(node.right , temp.key) 
    
        return node  


    def length(self):
        # Wrapper function
        if self.root:
            return self._length(self.root)
        else:
            return 0

    def _length(self, node):
        if node:
            return 1 + self._length(node.right) + self._length(node.left)
        else:
            return 0


    def contains(self, key):
        if self.root:
            if self._get(self.root, key) == None:
                return False
            return True
        else:
            return False


    def minValueNode(self, node): 
        current = node 
        # loop down to find the leftmost leaf 
        while(current.left is not None): 
            current = current.left 
    
        return current

class Node:
    def __init__(self):
        self.key = None
        self.val = None
        self.left = None
        self.right = None