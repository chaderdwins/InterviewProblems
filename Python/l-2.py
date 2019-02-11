# You are given two non-empty linked lists representing two non-negative integers. 
# The digits are stored in reverse order and each of their nodes contain a single digit. 
# Add the two numbers and return it as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example:
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def addTwoNumbers(self, l1: 'ListNode', l2: 'ListNode') -> 'ListNode':
        dummy_node = temp = ListNode(0)
        stack1, stack2 = [], []
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        while l2:
            stack2.append(l2.val)
            l2 = l2.next
        k = len(stack1)
        for i in range(len(stack1)):
            stack1[i] = str(stack1[i])
        stack1 = int(''.join(stack1)[::-1])

        for i in range(len(stack2)):
            stack2[i] = str(stack2[i])
        stack2 = int(''.join(stack2)[::-1])
        stack = str(stack1 + stack2)
        li = []
        for char in stack:
            li.append(int(char))
        print(li)
        while li:
            new_node = ListNode(li.pop())
            temp.next = new_node
            temp = new_node
        return dummy_node.next

        
