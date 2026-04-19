# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        cnt = 0
        k_smallest = -1

        def dfs(root, k):
            nonlocal cnt
            nonlocal k_smallest
            if not root:
                return

            dfs(root.left, k)
            cnt += 1
            if cnt == k:
                k_smallest = root.val
                return
            dfs(root.right, k)

        dfs(root, k)
        return k_smallest