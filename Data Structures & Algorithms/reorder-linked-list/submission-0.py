# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = head
        while fast and fast.next:
            slowM1 = slow
            slow = slow.next
            fast = fast.next.next
        
        curr = slow.next
        prev = slow.next = None
        
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        h1 = head
        while prev:

            th1, tp1 = h1.next, prev.next
            h1.next = prev
            prev.next = th1
            h1, prev = th1, tp1

        return None