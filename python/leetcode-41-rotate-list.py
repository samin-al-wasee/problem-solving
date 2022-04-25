# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None:
            return head
        length = 0
        current_node = head
        while current_node is not None:
            length += 1
            if current_node.next is None:
                current_node.next = head
                break
            current_node = current_node.next
        current_node = head
        rotation = k % length
        for i in range(length - rotation - 1):
            current_node = current_node.next
        head = current_node.next
        current_node.next = None
        return head
        