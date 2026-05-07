class Solution:
    def __init__(self) -> None:
        self.word_len = 0
        self.used = set()

    def dfs(self, board, i, j, word):
        # base case
        if self.word_len == len(word) - 1:
            return True

        self.used.add((i, j))
        for a, b in [[i + 1, j], [i - 1, j], [i, j + 1], [i, j - 1]]:
            if 0 <= a < len(board) and 0 <= b < len(board[0]) and (a, b) not in self.used and word[self.word_len+1] == board[a][b]:
                self.word_len += 1
                ans = self.dfs(board, a, b, word)
                self.word_len -= 1
                if ans:
                    return True
        self.used.remove((i, j))
        return False


    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    ans = self.dfs(board, i, j, word)
                    if ans:
                        return True
                
        return False

'''
[["A","B","C","E"],
 ["S","F","C","S"],
 ["A","D","E","E"]]


'''