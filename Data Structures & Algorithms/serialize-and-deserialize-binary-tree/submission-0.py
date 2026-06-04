# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# dfs + preorder traversal
class Codec:
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if root is None:
            return "#"

        left = self.serialize(root.left)
        right = self.serialize(root.right)
        return str(root.val) + "," + left + "," + right

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        def helper(data_list):
            if data_list[0] == "#":
                data_list.pop(0)
                return None
            
            node = TreeNode(int(data_list[0]))
            data_list.pop(0)
            node.left = helper(data_list)
            node.right = helper(data_list)
            return node

        data_list = list(data.split(","))
        return helper(data_list)


        