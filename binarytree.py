
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_heap_util(node: TreeNode) -> bool:
    if not node:
        return True
    
    if node.left and node.left.val > node.val:
        return False
    if node.right and node.right.val > node.val:
        return False
    
    return is_heap_util(node.left) and is_heap_util(node.right)

def is_heap(root: TreeNode) -> bool:
    return is_heap_util(root)


root = TreeNode(10, TreeNode(9), TreeNode(8))
print(is_heap(root))  