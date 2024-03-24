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
            