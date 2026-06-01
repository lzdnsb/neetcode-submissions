# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# in a node: return max(leftmax + node.val, rightmax + node.val, node.val)
# traversal(node) returns the maximum downward path sum starting from this node, where the path can only extend to one side.

# update golbal maximum: I can take both the left and right contributions, because the path is allowed to bend at this node.

# post-order traversal

class Solution:
    def __init__(self) -> None:
        self.max_path_sum = float("-inf")

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        _ = self.traversal(root)

        return self.max_path_sum


    def traversal(self, node):
        if not node:
            return 0

        leftmax = self.traversal(node.left)
        rightmax = self.traversal(node.right)

        a, b, c = leftmax + node.val, rightmax + node.val, leftmax + node.val + rightmax
        self.max_path_sum = max(self.max_path_sum, a, b, c, node.val)
        return max(a, b, node.val)
        
        