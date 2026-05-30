class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        zero_row = set()
        zero_col = set()
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    zero_row.add(i)
                    zero_col.add(j)  
                     

        for i in range(m):
            if i in zero_row:
                for k in range(n):
                    matrix[i][k] = 0

        for j in range(n):
            if j in zero_col:
                for k in range(m):
                    matrix[k][j] = 0

        return

# [[0,1,2,0],
#  [3,4,5,2],
#  [1,3,1,5]]     