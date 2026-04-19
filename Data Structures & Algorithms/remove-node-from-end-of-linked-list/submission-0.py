# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head
        fast, slow = dummy, dummy
        for _ in range(n):
            if fast:
                fast = fast.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next
        if slow and slow.next:
            slow.next = slow.next.next
        

        return dummy.next

