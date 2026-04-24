"""
# Definition for a Node.
from types import new_class
from types import new_class
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

# class Solution:
#     def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
#         if not node:
#             return

#         old2new = {}

#         def dfs(node):
#             if node in old2new:
#                 return old2new[node]

#             new_node = Node(node.val)
#             old2new[node] = new_node
#             for nei in node.neighbors:
#                 new_node.neighbors.append(dfs(nei))
#             return new_node

#         return dfs(node)

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return
        old2new = {}
        q = deque()
        q.append((node, None))
        while q:
            a, prev = q.popleft()
            if a in old2new:
                if prev:
                    prev.neighbors.append(old2new[a])
                continue
            new_node = Node(a.val)
            old2new[a] = new_node
            if prev:
                prev.neighbors.append(new_node)
            for nei in a.neighbors:
                if nei:
                    q.append((nei,new_node))
        return old2new[node]




