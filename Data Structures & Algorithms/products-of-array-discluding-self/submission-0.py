class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixProduct = [1]
        for i in range(1, len(nums)):
            prefixProduct.append(prefixProduct[i-1] * nums[i-1])

        #ans = [1] * len(nums)
        postProduct = 1
        for i in range(len(nums)-1, -1, -1):
            prefixProduct[i] *= postProduct
            postProduct *= nums[i]
        return prefixProduct
