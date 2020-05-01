class Map:
    name = "MR BST"
    def __init__(self, size):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size


    def __setitem__(self, k, v):
        self.put(k, v)
    
    def __delitem__(self, key):
        self.delete(key)

    def put(self, key, val):
        if self.root:
            self._put(key, val, self.root)
        else:
            self.root = TreeNode(key, val)
            self.size = self.size + 1

    def _put(self, key, val, current_node):
        if key < current_node.key:
            if current_node.has_left_child():
                self._put(key, val, current_node.left_child)
            else:
                current_node.left_child = TreeNode(key, val, parent=current_node)
        else:
            if current_node.has_right_child():
                self._put(key, val, current_node.right_child)
            else:
                current_node.right_child = TreeNode(key, val, parent=current_node)

    def get(self,key):
        if self.root:
            res = self._get(key, self.root)
            if res:
                return res.val
            else:
                return None
        else:
            return None

    def _get(self, key, current_node):
        if not current_node:
            return None
        elif current_node.key == key:
            return current_node
        elif key < current_node.key:
            return self._get(key, current_node.left_child)
        else:
            return self._get(key, current_node.right_child)

    def __contains__(self, key):
        if self._get(key, self.root):
            return True
        else:
            return False

    def contains(self, key):
        if self.root:
            if self._get(key, self.root) == None:
                return False
            return True
        else:
            return False

    def delete(self, key):
        # Wrapper function
        self._delete(self.root, key)

    def _delete(self, node, key):
        if node is None: 
            return node
  
        if key < node.key: 
            node.left_child = self._delete(node.left_child, key) 

        elif(key > node.key): 
            node.right_child = self._delete(node.right_child, key) 
    
        else: 
            if node.left_child is None: 
                temp = node.right_child  
                node = None 
                return temp  
                
            elif node.right_child is None : 
                temp = node.left_child  
                node = None
                return temp 
     
            temp = self.minValueNode(node.right_child) 
    
            node.key = temp.key
            node.val = temp.val

            node.right_child = self._delete(node.right_child , temp.key) 
    
        return node 

    def minValueNode(self, node): 
        current = node 
        # loop down to find the leftmost leaf 
        while(current.left_child is not None): 
            current = current.left_child 
    
        return current 

class TreeNode:
    def __init__(self, key, val, left = None, right = None, parent = None):
        self.key = key
        self.val = val
        self.left_child = left
        self.right_child = right
        self.parent = parent

    def has_left_child(self):
        return self.left_child

    def has_right_child(self):
        return self.right_child

    def is_left_child(self):
        return self.parent and self.parent.left_child == self

    def is_right_child(self):
        return self.parent and self.parent.right_child == self

    def is_root(self):
        return not self.parent

    def is_leaf(self):
        return not (self.right_child or self.left_child)

    def has_any_children(self):
        return self.right_child or self.left_child

    def has_both_children(self):
        return self.right_child and self.left_child

    def replace_node_data(self, key, value, lc, rc):
        self.key = key
        self.val = value
        self.left_child = lc
        self.right_child = rc

        if self.has_left_child():
            self.left_child.parent = self
        if self.has_right_child():
            self.right_child.parent = self
