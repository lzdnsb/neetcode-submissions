# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         if len(s) == 0:
#             return 0
#         longest = 0
#         record = defaultdict(int)
#         start = 0
#         for i in range(len(s)):
#             if s[i] not in record:
#                 record[s[i]] = i
#             else:
#                 longest = max(longest, i - start)
#                 prev = record[s[i]] + 1
#                 for j in range(start, record[s[i]] + 1): 
#                     del record[s[j]]
#                 start = prev
#                 record[s[i]] = i
#         longest = max(longest, len(s) - start)
#         return longest

# Instead of removing characters one by one when we see a repeat, we can jump the left pointer directly to the correct position.
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        longest = 0
        record = {}
        for right in range(len(s)):
            # shrink the windoe if have duplicate ch
            if s[right] in record:
                left = max(left, record[s[right]] + 1)
            # add to window
            record[s[right]] = right
            # update the longest
            longest = max(longest, right - left + 1)
        return longest


