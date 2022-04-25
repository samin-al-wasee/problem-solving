# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodes = []
        current_node = head
        while current_node is not None:
            nodes.append(current_node)
            current_node = current_node.next
        if n == len(nodes):
            return nodes[-n].next
        nodes[-n-1].next = nodes[-n].next
        return head
        