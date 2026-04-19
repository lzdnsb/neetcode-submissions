# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# cut the linked-list in half
# reversed the 2nd part
# merged the 1st part and the reversed 2nd part
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # use fast-slow pointer to cut the linked-lsit in half
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reversed from slow.next to fast (2nd part)
        pre, p = None, slow.next
        while p:
            cur = p.next
            p.next = pre
            pre = p
            p = cur
        slow.next = None

        # merged head and cur (tail)
        h = head
        t = pre
        while t and h:
            cur = h.next
            h.next = t
            h = cur
            cur = t.next
            t.next = h
            t = cur

        return 

# 0,1,2,3
# 6,5,4

        # 0,1,2,3,4,5
        # 0,5,1,4,2,3