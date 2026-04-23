class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i, j):
            grid[i][j] = -1
            for x, y in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                if 0 <= i + x < len(grid) and 0 <= j + y < len(grid[0]) and grid[i+x][j+y] == '1':
                    dfs(i + x, j + y)
            return

        m, n = len(grid), len(grid[0])
        cnt = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    dfs(i , j)
                    cnt += 1

        return cnt

        
