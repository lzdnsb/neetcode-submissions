# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
A Binary Search Tree isn’t just about each node being smaller or larger than its parent —
every node must fit within a valid value range decided by all its ancestors.
'''
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def helper(node, l, r):
            if not node:
                return True
            if node.val > l and node.val < r:
                return helper(node.left, l , node.val) and helper(node.right, node.val, r)
            return False

        return helper(root, -float('inf'), float('inf'))
        