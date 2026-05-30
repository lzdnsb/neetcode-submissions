'''
First, we reverse the matrix vertically, meaning the first row becomes the last, the second row becomes the second last, and so on. 
Next, we transpose the reversed matrix, meaning rows become columns and columns become rows. 
'''

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        for i in range(m//2):
            matrix[i], matrix[m - i - 1] = matrix[m - i - 1], matrix[i]

        for i in range(m):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        return