import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter_nums = Counter(nums)
        output = []
        for ele, cnt in counter_nums.items():
            heapq.heappush(output, (cnt, ele))
            if len(output) > k:
                heapq.heappop(output)
        ans = []
        for cnt, ele in output:
            ans.append(ele)
        return ans