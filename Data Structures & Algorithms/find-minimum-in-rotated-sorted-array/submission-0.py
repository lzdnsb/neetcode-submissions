class Solution:
    def findMin(self, nums: List[int]) -> int:
        min_element = 0
        l, r = 0, len(nums)-1
        while l <= r:
            mid = (l+r) // 2
            if nums[mid] >= nums[l] and nums[mid] >= nums[r]: # the left part of the array is sorted and the min_ele is on the right part
                l = mid + 1
            else:
                r = mid
        min_element = nums[r]
        return min_element


# 1,2,3,4,5,6
# 6,1,2,3,4,5
# 5,6,1,2,3,4
# 4,5,6,1,2,3
# 3,4,5,6,1,2
# 2,3,4,5,6,1

# 1,2,3,4,5
# 5,1,2,3,4
# 4,5,1,2,3
# 3,4,5,1,2
# 2,3,4,5,1
