# "1" - "9"
# "10" - "19"
# "20" - "26"
class Solution:
    def numDecodings(self, s: str) -> int:
        # dp[i] means how many ways we can decode s[0:i+1] 
        dp = [0] * len(s)
        # base case
        if s[0] == "0":
            return 0
        dp[0] = 1
        for i in range(1, len(s)):
            if s[i] != "0": # s[i] is in "1" - "9"
                dp[i] += dp[i-1]
            # group s[i-1] and s[i] together
            if (s[i-1] == "2" and "0" <= s[i] <= "6") or s[i-1] == "1":
                if i - 2 >= 0: 
                    dp[i] += dp[i-2]
                else:
                    dp[i] += 1
        return dp[-1]
        