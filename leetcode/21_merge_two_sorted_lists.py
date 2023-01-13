### the good way of doing this:
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            
            tail = tail.next
        
        if list1:
            tail.next = list1
        else:
            tail.next = list2

        return dummy.next


### the wrong way (my first try)

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        one = list1
        two = list2
        ans = None

        head = ans
        while one or two:
            if not ans:
                if not one:
                    ans = two
                    two = two.next
                elif not two:
                    ans = one
                    one = one.next
                elif one.val < two.val or one.val == two.val:
                    ans = one
                    one = one.next
                elif two.val < one.val:
                    ans = two
                    two = two.next
                
                head = ans

            else:
                if not one:
                    ans.next = two
                    ans = ans.next
                    two = two.next
                elif not two:
                    ans.next = one
                    ans = ans.next
                    one = one.next
                elif one.val < two.val or one.val == two.val:
                    ans.next = one
                    ans = ans.next
                    one = one.next
                elif two.val < one.val:
                    ans.next = two
                    ans = ans.next
                    two = two.next
    
        return head