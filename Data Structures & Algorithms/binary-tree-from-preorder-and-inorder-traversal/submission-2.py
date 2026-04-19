# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class Solution:
#     def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
#         if not preorder or not inorder: # this is also correct : len(preorder) == 0 or len(inorder) == 0
#             return None
#         node = TreeNode(preorder[0])
#         idx = inorder.index(preorder[0])
#         node.left = self.buildTree(preorder[1: idx + 1], inorder[0: idx])
#         node.right = self.buildTree(preorder[idx + 1: ], inorder[idx + 1:])
#         return node

# optimization: 1) donot do sliding, Only pass the index of the left and right boundaries; 
# 2) Use a hashmap to pre-store the position of each value in the inorder to avoid index()
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # use hashmap tp store the position of each value in the inorder to avoid index()
        val2idx = {k: v for v, k in enumerate(inorder)}

        pre_idx = 0 # the position of root in preorder
        def dfs(l, r): # [l, r] is the range of inorder
            nonlocal pre_idx
            if l > r: # no need: or pre_idx >= len(preorder)
                return None
            node = TreeNode(preorder[pre_idx])
            idx = val2idx[preorder[pre_idx]]
            pre_idx += 1
            node.left = dfs(l, idx-1)
            node.right = dfs(idx+1, r)
            return node

        return dfs(0, len(inorder)-1)


