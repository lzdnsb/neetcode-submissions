class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        val2idx = defaultdict(int)
        for i, num in enumerate(nums):
            if (target - num) in val2idx:
                return [val2idx[target-num], i]
            else:
                val2idx[num] = i
        return [-1, -1]