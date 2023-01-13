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