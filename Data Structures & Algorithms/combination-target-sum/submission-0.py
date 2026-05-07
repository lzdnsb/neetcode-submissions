class Solution:
    def __init__(self) -> None:
        self.res = []
        self.track = []
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.combination_helper(nums, 0, target)
        return self.res
        
    def combination_helper(self, nums, start, target):
        # base case
        if sum(self.track) == target:
            self.res.append(self.track.copy())
            return
        if sum(self.track) > target:
            return
        
        for i in range(start, len(nums)):
            self.track.append(nums[i])
            self.combination_helper(nums, i, target)
            self.track.pop()