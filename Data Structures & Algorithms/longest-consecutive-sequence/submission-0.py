class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest_length = 0
        for num in nums:
            if num - 1 not in nums_set:
                cur_length = 1
                while num + cur_length in nums_set:
                    cur_length += 1
                longest_length = max(longest_length, cur_length)
        return longest_length