# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
        current=head
        for _ in range(k):
            if not current:
                return head
            current=current.next
        prev=None
        current=head
        
        for _ in range(k):
            next_node=current.next
            current.next=prev
            prev=current
            current=next_node
        head.next=self.reverseKGroup(current,k)
        return prev  
        