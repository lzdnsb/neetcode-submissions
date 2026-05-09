class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(i, j, idx):
            nonlocal used
            # base case
            if idx == len(word) - 1 and board[i][j] == word[idx]:
                return True

            used.add((i, j))
            for a, b in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if 0 <= a < len(board) and 0 <= b < len(board[0]) and board[a][b] == word[idx + 1] and (a, b) not in used:
                    ans = dfs(a, b, idx + 1)
                    if ans:
                        return True 
            used.remove((i, j))
            return False

        used = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    res = dfs(i, j, 0)
                    if res:
                        return True
        return False