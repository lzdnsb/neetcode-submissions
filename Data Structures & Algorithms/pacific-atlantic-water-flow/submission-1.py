# dfs
# we can start from the border, the check if water can flow to each cell.

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def dfs(i, j, ocean, h_pre): # only if water can flow to that cell, we add it to the set()
            if i < 0 or i >= len(heights) or j < 0 or j >= len(heights[0]) or heights[i][j] < h_pre or (i, j) in ocean:
                return
            ocean.add((i, j))
            dfs(i + 1, j, ocean, heights[i][j])
            dfs(i - 1, j, ocean, heights[i][j])
            dfs(i, j + 1, ocean, heights[i][j])
            dfs(i, j - 1, ocean, heights[i][j])


        pacific = set()
        atlantic = set()
        m, n = len(heights), len(heights[0])
        for i in range(m):
            dfs(i, 0, pacific, heights[i][0])
            dfs(i, n-1, atlantic, heights[i][n-1])
        for j in range(n):
            dfs(0, j, pacific, heights[0][j])
            dfs(m-1, j, atlantic, heights[m-1][j])

        # get results
        ans = []
        for i in range(m):
            for j in range(n):
                if (i, j) in pacific and (i, j) in atlantic:
                    ans.append([i, j])
        return ans