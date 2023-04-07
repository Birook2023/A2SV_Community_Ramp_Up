# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def nested(node, left, right):
            if not node:
                return True
            if node.val >= right or node.val <= left:
                return False
            bool1 = nested(node.left, left, node.val)
            bool2 = nested(node.right, node.val, right)
            return bool1 and bool2
        left = float('-inf')
        right = float('inf')
        
        return nested(root, left, right)
