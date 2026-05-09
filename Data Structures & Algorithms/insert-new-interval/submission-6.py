# '''
# if end_i >= start_new or start_j <= end_new: overlap
#     start_merge = min(start_i, start_new)
#     end_merge = max(end_j, end_new)
# otherwise:
#     append the interval to the output list
# '''

# class Solution:
#     def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
#         output = []
#         i = 0
#         start_new, end_new = newInterval[0], newInterval[1]
#         while i < len(intervals):
#             start_i, end_i = intervals[i][0], intervals[i][1]
#             if end_i < start_new: # non-overlap
#                 output.append(intervals[i])
#                 i += 1
#             elif end_i >= start_new and start_i <= end_new: # overlap
#                 if len(output) == 0 or (len(output) != 0 and output[-1][1] < min(start_i, start_new)):
#                     start_merge = min(start_i, start_new)
#                     end_merge = max(end_i, end_new)
#                     output.append([start_merge, end_merge])
#                     i += 1
#                 else:
#                     output[-1][1] = max(output[-1][1], end_i)
#                     i += 1
#             else: # non-overlap and insert newInterval
#                 if len(output) == 0:
#                     output.append(newInterval)
#                     output.append(intervals[i])
#                     i += 1
#                 else:
#                     if not output or (start_new > output[-1][1] and end_new < start_i):
#                         output.append(newInterval)
#                     else:
#                         output.append(intervals[i])
#                         i += 1

#         # base case: start_new > intervals[-1][1]
#         if not intervals or start_new > intervals[-1][1]:
#             output.append(newInterval)
#         return output


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        output = []
        i = 0
        start_new, end_new = newInterval[0], newInterval[1]
        while i < len(intervals):
            start_i, end_i = intervals[i][0], intervals[i][1]
            if end_i < start_new or start_i > end_new: # non-overlap
                # special case: insert newInterval without overlap
                if (not output and end_new < start_i) or (output and start_new > output[-1][1] and end_new < start_i):
                    output.append(newInterval)
                output.append(intervals[i])
                i += 1
            else: # overlap, need to merge intervals and newInterval
                start_merge, end_merge = min(start_i, start_new), max(end_i, end_new)
                i += 1
                if i < len(intervals):
                    start_i, end_i = intervals[i][0], intervals[i][1]
                while i < len(intervals) and start_i <= end_new:
                    start_merge = min(start_merge, start_i)
                    end_merge = max(end_merge, end_i)
                    i += 1
                    if i < len(intervals):
                        start_i, end_i = intervals[i][0], intervals[i][1]
                output.append([start_merge, end_merge])
        # base case: start_new > intervals[-1][1]
        if not intervals or start_new > intervals[-1][1]:
            output.append(newInterval)
        return output








