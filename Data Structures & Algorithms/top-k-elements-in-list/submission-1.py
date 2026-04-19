# import heapq
# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         counter_nums = Counter(nums)
#         output = []
#         for ele, cnt in counter_nums.items():
#             heapq.heappush(output, (cnt, ele))
#             if len(output) > k:
#                 heapq.heappop(output)
#         ans = []
#         for cnt, ele in output:
#             ans.append(ele)
#         return ans

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter_nums = Counter(nums)
        fre = [[] for _ in range(len(nums)+1)]
        for ele, cnt in counter_nums.items():
            fre[cnt].append(ele)
        ans = []
        for i in range(len(fre)-1, -1, -1):
            for num in fre[i]:
                ans.append(num)
                if len(ans) == k:
                    return ans
