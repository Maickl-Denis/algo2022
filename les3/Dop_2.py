# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head == None:
            return head
        
        count = 0
        hd = head
        while hd != None:
            hd = hd.next
            count += 1
        
        mid = count // 2
        
        hd = head
        while mid != 0:
            hd = hd.next
            mid -= 1
            
        return hd