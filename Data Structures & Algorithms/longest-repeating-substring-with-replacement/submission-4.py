'''
对每个窗口，判断
窗口长度 - 窗口内最高频字符次数 <= k
是否成立。
'''

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        l = 0
        max_freq = 0
        longest = 0

        for r in range(len(s)):
            # add to window
            count[s[r]] += 1
            # calculate len(window) - max_freq
            max_freq = max(max_freq, count[s[r]])
            while k < (r - l + 1) - max_freq: # shrink the window
                count[s[l]] -= 1
                l += 1
            longest = max(longest, r - l + 1)
        return longest


        