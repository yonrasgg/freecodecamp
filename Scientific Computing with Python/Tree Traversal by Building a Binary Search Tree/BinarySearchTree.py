class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        
class BinarySearchTree:
    def __init__(self):
        self.root = None
        
    def insert(self, key):
        self.root = self._insert(self.root, key)
        
    def _insert(self, node, key):
        if node is None:
            return TreeNode(key)
        if key < node.key:     
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        return node
    
    def search(self, key):
        self._search(self.root, key)
        return self._search(self.root, key)
    
    def _search(self, node, key):
        if node is None or node.key == key:
            return node