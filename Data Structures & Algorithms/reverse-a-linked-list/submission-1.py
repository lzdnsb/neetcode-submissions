# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_head = ListNode(-1) # dummy head
        pre= new_head
        p = head
        while p:
            nxt = pre.next
            new_node = ListNode(p.val)
            pre.next = new_node
            new_node.next = nxt
            p = p.next

        return new_head.next

# class Solution:
#     def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         new_head = ListNode(-1)
#         if not head:
#             return head
#         pre, p = head, head.next
#         pre.next = None
#         while p:
#             cur = p.next
#             p.next = pre
#             pre = p
#             p = cur
#         return pre
        



