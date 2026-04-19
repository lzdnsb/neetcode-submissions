class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        times = defaultdict(int)
        for num in nums:
            times[num] += 1
            if times[num] > 1:
                return True
            
        return False