# check cycle + all the nodes are visited
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # build graph
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        # check cycle
        visited = set()
        def dfs(i, prev):
            nonlocal check
            if i in visited:
                return False
            visited.add(i)
            for j in graph[i]:
                if j != prev:
                    ans = dfs(j, i)
                    if not ans:
                        return False
            # visited.remove(i)
            # check += 1
            return True

        check = 0
        ans = dfs(0, -1)
        if not ans: # has cycle
            return False
        
        return len(visited) == n        
