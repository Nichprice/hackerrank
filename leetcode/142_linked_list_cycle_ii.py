class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return

        slow, fast = head, head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast: break

        slow2 = head

        while slow:
            if slow == slow2: return
            slow = slow.next
            slow2 = slow2.next.next

        return