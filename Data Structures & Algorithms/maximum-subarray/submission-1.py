class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        largest_sum = min(nums)
        cur_sum = 0
        for i in range(len(nums)):
            cur_sum += nums[i]
            if cur_sum < nums[i]:
                cur_sum = nums[i]
            largest_sum = max(largest_sum, cur_sum)
        return largest_sum

