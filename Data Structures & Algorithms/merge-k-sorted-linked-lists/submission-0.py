# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        p = dummy
        pq = []
        for i in range(len(lists)):
            heapq.heappush(pq, (lists[i].val, i, lists[i])) # val, i-th linked-list, head
        
        while len(pq) > 0:
            value, i_list, list_node = heapq.heappop(pq)
            p.next = ListNode(value)
            p = p.next
            if list_node.next:
                heapq.heappush(pq, (list_node.next.val, i_list, list_node.next))
        return dummy.next


