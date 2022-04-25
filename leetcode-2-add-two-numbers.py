# https://leetcode.com/problems/add-two-numbers/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        result_head = ListNode()
        current_bit = result_head
        while l1 is not None or l2 is not None:
            if l1 is None:
                current_bit.val = (carry + l2.val) % 10
                carry = (carry + l2.val) // 10
                if l2.next is not None:
                    current_bit.next = ListNode()
                    current_bit = current_bit.next
                l2 = l2.next
            elif l2 is None:
                current_bit.val = (carry + l1.val) % 10
                carry = (carry + l1.val) // 10
                if l1.next is not None:
                    current_bit.next = ListNode()
                    current_bit = current_bit.next
                l1 = l1.next
            else:
                current_bit.val = (carry + l1.val + l2.val) % 10
                carry = (carry + l1.val + l2.val) // 10
                if l1.next is not None or l2.next is not None:
                    current_bit.next = ListNode()
                    current_bit = current_bit.next
                l1 = l1.next
                l2 = l2.next
        if carry == 1:
            current_bit.next = ListNode(1)
        return result_head
    