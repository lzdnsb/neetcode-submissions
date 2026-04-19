# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class Solution:
#     def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
#         cnt = 0
#         k_smallest = -1

#         def dfs(root, k):
#             nonlocal cnt
#             nonlocal k_smallest
#             if not root or cnt == k: # if ans found, return here
#                 return

#             dfs(root.left, k)
#             if cnt == k: # if ans found, return here
#                 return 

#             cnt += 1
#             if cnt == k:
#                 k_smallest = root.val
#                 return # 回到父节点那一层后，父节点后面的递归还可能继续执行
#             dfs(root.right, k)

#         dfs(root, k)
#         return k_smallest

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        cnt = 0
        k_smallest = -1

        def dfs(root, k):
            nonlocal cnt
            nonlocal k_smallest
            if not root:
                return False

            if dfs(root.left, k):
                return True

            cnt += 1
            if cnt == k:
                k_smallest = root.val
                return True
            return dfs(root.right, k)

        dfs(root, k)
        return k_smallest




