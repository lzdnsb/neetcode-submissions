class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        longest = 0
        record = defaultdict(int)
        start = 0
        for i in range(len(s)):
            if s[i] not in record:
                record[s[i]] = i
            else:
                longest = max(longest, i - start)
                prev = record[s[i]] + 1
                for j in range(start, record[s[i]] + 1):
                    del record[s[j]]
                start = prev
                record[s[i]] = i
        longest = max(longest, len(s) - start)
        return longest