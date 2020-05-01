import random

class Map:
    name = "Balanced Search Tree"
    def __init__(self, size):
        self.root = None

    def put(self, key, val):
        # Wrapper function
        if self.root:
            self.root = self._put(self.root, key, val)
        else:
            self.root = Node()
            self.root.key = key
            self.root.val = val

    def _put(self, node, key, val):
        if key == node.key:
            node.val = val
        elif key > node.key:
            if node.right:
                node.right = self._put(node.right, key, val)
            else:
                node.right = Node()
                node.right.key = key
                node.right.val = val
        else:
            if node.left:
                node.left = self._put(node.left, key, val)
            else:
                node.left = Node()
                node.left.key = key
                node.left.val = val

        # Step 2
        node.height = 1 + max(self.getheight(node.left), self.getheight(node.right))

        # Step 3
        balance = self.getbalance(node)

        # Step 4

        # Case 1
        if balance > 1 and key < node.left.key:
            return self.rightRotate(node)

        # Case 2
        if balance < -1 and key > node.right.key:
            return self.leftRotate(node)

        # Case 3
        if balance > 1 and key > node.left.key:
            node.left = self.leftRotate(node.left)
            return self.rightRotate(node)

        # Case 3
        if balance < -1 and key < node.right.key:
            node.right = self.rightRotate(node.right)
            return self.leftRotate(node)

        return node


    def leftRotate(self, z):
        y = z.right
        T2 = y.left

        # Performes rotation
        y.left = z
        z.right = T2

        # Update Heights
        z.height = 1 + max(self.getheight(z.left), self.getheight(z.right))
        y.height = 1 + max(self.getheight(y.left), self.getheight(y.right))

        return y

    def rightRotate(self, z):
        y = z.left
        T3 = y.right

        # Performes rotation
        y.right = z
        z.left = T3

        # Update Heights
        z.height = 1 + max(self.getheight(z.left), self.getheight(z.right))
        y.height = 1 + max(self.getheight(y.left), self.getheight(y.right))

        return y

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

        if node is None:
            return node

        # Step 2 update height
        node.height = 1 + max(self.getheight(node.left), self.getheight(node.right))

        # Step 3 get balance
        balance = self.getbalance(node)

        # Step 4

        # Case 1
        if balance > 1 and self.getbalance(node.left) >= 0:
            return self.rightRotate(node)

        # Case 2
        if balance < -1 and self.getbalance(node.right) <= 0:
            return self.leftRotate(node)

        # Case 3
        if balance > 1 and self.getbalance(node.left) < 0:
            node.left = self.leftRotate(node.left)
            return self.rightRotate(node)

        # Case 4
        if balance < -1 and self.getbalance(node.right) > 0:
            node.right = self.rightRotate(node.right)
            return self.leftRotate(node)
    
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


    def getheight(self, node):
        if not node:
            return 0
        else:
            return node.height

    def getbalance(self, node):
        if not node:
            return 0
        else:
            return self.getheight(node.left) - self.getheight(node.right)

class Node:
    def __init__(self):
        self.height = 1
        self.key = None
        self.val = None
        self.left = None
        self.right = None