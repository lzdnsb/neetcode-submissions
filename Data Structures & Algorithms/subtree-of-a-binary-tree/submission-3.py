# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class Solution:   
#     def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
#         # traverse tree 'root', compared root.val and subRoot.val
#         if self.isSameTree(root, subRoot):
#             return True
#         if root:
#             return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
#         return False
        
    
#     def isSameTree(self, p, q):
#         if not p and not q:
#             return True
#         if p and q and p.val == q.val:
#             return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
#         return False

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # serialization: tree -> string
        s_root = self.serializeTree(root)
        s_sub = self.serializeTree(subRoot)

        # z-algorithm: find substring in a string
        combined = s_sub + '@' + s_root
        z = self.zFunction(combined)
        for i in range(len(s_sub) + 1, len(combined)):
            if z[i] == len(s_sub):
                return True
        return False

    def serializeTree(self, node):
        if not node:
            return "$#"
        return "$" + str(node.val) + self.serializeTree(node.left) + self.serializeTree(node.right)

    def zFunction(self, s):
        z = [0] * len(s)
        l, r = 0, 0
        for i in range(1, len(s)):
            # i in z-box [l ,r]
            if i <= r:
                z[i] = min(r - i + 1, z[i - l])
            # expand range
            while i + z[i] < len(s) and s[i + z[i]] == s[z[i]]:
                z[i] += 1
            # update [l ,r]
            if i + z[i] - 1 > r:
                l, r = i, i + z[i] - 1
        return z






