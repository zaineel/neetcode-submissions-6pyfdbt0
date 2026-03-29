# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        length = 0
        while curr:
            length += 1
            curr = curr.next
        node_to_remove = length-n
        curr = head
        if n == length:
            return head.next
        for i in range(length):
            if i == node_to_remove - 1:
                curr.next = curr.next.next
                return head
            curr = curr.next

        return head



        