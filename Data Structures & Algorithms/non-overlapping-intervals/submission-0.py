class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        i = 1
        prev = 0
        cnt = 0
        while i < len(intervals):
            if intervals[i][0] < intervals[prev][1]:  # overlap, rm the longer interval
                cnt += 1
                if intervals[i][1] < intervals[prev][1]:
                    prev = i 
            else:
                prev = i
            i += 1
        return cnt
            
                
