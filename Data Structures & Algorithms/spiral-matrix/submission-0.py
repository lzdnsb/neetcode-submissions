class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        total = m * n
        i = 0
        # dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        right, down, left, top = n - 1, m - 1, 0, 1
        output = []
        r, c = 0, 0
        while i < total:
            while c <= right and i < total:
                output.append(matrix[r][c])
                c += 1
                i += 1
            right -= 1
            r += 1
            c -= 1
            while r <= down and i < total:
                output.append(matrix[r][c])
                r += 1
                i += 1
            down -= 1
            r -= 1
            c -= 1
            while c >= left and i < total:
                output.append(matrix[r][c])
                c -= 1
                i += 1
            left += 1
            r -= 1
            c += 1
            while r >= top and i < total:
                output.append(matrix[r][c])
                r -= 1
                i += 1
            top += 1
            r += 1
            c += 1
        return output
