"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
# use minheap to save the end time of each room
# for each meeting, put it to the room with earliest end time without conflicts
# return len(minheap) as the number of rooms
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        rooms = [] # minheap
        intervals.sort(key=lambda x: x.start)
        for i in range(len(intervals)):
            if not rooms:
                heapq.heappush(rooms, intervals[i].end)
            else:
                # try to arrange the current interval to the room with the earliest end time
                if rooms[0] > intervals[i].start: # need a new room
                    heapq.heappush(rooms, intervals[i].end)
                else:
                    heapq.heappop(rooms)
                    heapq.heappush(rooms, intervals[i].end)  
        return len(rooms)




