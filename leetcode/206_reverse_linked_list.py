# class Solution:
#     def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         prev, curr = None, head

#         while curr:
#             nxt = curr.next
#             curr.next = prev
#             prev = curr
#             curr = nxt
        
#         return prev

## redoing this now that I know what a singly linked list is

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev