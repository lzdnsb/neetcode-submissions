# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         largest_sum = min(nums)
#         cur_sum = 0
#         for i in range(len(nums)):
#             cur_sum += nums[i]
#             if cur_sum < nums[i]:
#                 cur_sum = nums[i]
#             largest_sum = max(largest_sum, cur_sum)
#         return largest_sum

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = nums.copy()
        # dp[i]: when choosing nums[i] as the last number in the subarray, the largest sum
        for i in range(1, len(nums)):
            dp[i] = max(dp[i-1] + nums[i], nums[i])
        return max(dp)