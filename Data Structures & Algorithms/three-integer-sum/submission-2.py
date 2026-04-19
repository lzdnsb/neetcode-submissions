class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        results = []
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left, right = i+1, len(nums)-1
            while left < right:
                if nums[left] + nums[right] == -nums[i]:
                    results.append([nums[i], nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    right -= 1
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1
                elif nums[left] + nums[right] < -nums[i]:
                    left += 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                else:
                    right -= 1
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1
        return results


        # [-5, -3, -2, -1, 0, 0, 0, 1, 1, 1, 3, 3, 4, 4, 4]