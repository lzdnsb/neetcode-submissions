# 普通的思路：逐个数位相加，保存进位的方法在python中的局限
# 1）python的整数不是32位的，而是“无限的”；这道题要求计算32-bit signed integer
# 2）考虑到有负数，应该使用补码表示进行运算

# 基础知识
# a ^ b: 不考虑进位的相加结果
# (a & b) << 1: 进位
# 所以 a + b = 上述两个结果的相加
# 一直加到carry=0结束
class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF # get 32-bit
        mask_positive = 0x7FFFFFFF
        res = a
        while b != 0:
            res = (a ^ b) & mask
            carry = (a & b) << 1
            a, b = res, carry & mask
        return res if res <= mask_positive else ~(res ^ mask)
        
# class Solution:
#     def getSum(self, a: int, b: int) -> int:
#         MASK = 0xFFFFFFFF
#         MAX_INT = 0x7FFFFFFF

#         while b != 0:
#             carry = (a & b) & MASK
#             a = (a ^ b) & MASK
#             b = (carry << 1) & MASK

#         return a if a <= MAX_INT else ~(a ^ MASK)


        # 101
            
