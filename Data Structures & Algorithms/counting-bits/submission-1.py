class Solution:
    def countBits(self, n: int) -> List[int]:
        cnt = [0] * (n+1)
        # base case
        if n >= 1:
            cnt[1] = 1
        for i in range(2, n+1):
            a = i % 2
            b = i // 2
            cnt[i] = a + cnt[b]
        return cnt