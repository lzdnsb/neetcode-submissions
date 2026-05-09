class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # step1: sort the intervals by start_i
        intervals.sort(key=lambda x: x[0])
        output = []
        # step2: traverse the intervals and merge overlap intervals
        i = 0
        while i < len(intervals):
            if not output:
                output.append(intervals[i])
            else:
                if intervals[i][0] > output[-1][1]:
                    output.append(intervals[i])
                else:
                    output[-1][1] = max(output[-1][1], intervals[i][1])
            i += 1
        return output