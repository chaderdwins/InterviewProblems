# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: 'ListNode') -> 'ListNode':
        if not head:
            return None
        li = []
        current = head
        prev = None
        while current:
            if current.val not in li:
                li.append(current.val)
            else:
                prev.next = current.next
                current = prev
            prev = current
            current = current.next
        return li
            
        