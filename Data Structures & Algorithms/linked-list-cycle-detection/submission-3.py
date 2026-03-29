# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr = head
        set_of_nodes = set()
        while curr:
            if curr in set_of_nodes:
                return True
            else:
                set_of_nodes.add(curr)
            curr = curr.next
        return False
        