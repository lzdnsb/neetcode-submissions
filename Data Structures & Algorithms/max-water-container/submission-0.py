class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # water = (idx2 - idx1) * min(heights[idx1], heights[idx2])
        l, r = 0, len(heights)-1
        max_water = 0
        while l < r:
            cur_water = (r - l) * min(heights[l], heights[r])
            max_water = max(max_water, cur_water)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return max_water
            
