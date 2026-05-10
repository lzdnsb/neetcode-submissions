class Solution:
    def canJump(self, nums: List[int]) -> bool:
        mark = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if mark - i <= nums[i]:
                mark = i
        if mark == 0:
            return True
        return False