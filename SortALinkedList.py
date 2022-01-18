"""
BINARY SEARCH: SORT A LINKED LIST

Given a singly linked list of integers node, sort the nodes by their 
values in ascending order.

Constraints
n ≤ 100,000 where n is the number of nodes in node

Example 1
Input: node = [14, 13, 10]
Output: [10, 13, 14]
"""

class LLNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    def solve(self, node):
        # initialize pointer cursor to head of linkedlist
        cursor = node
        # initialize array values to store all node values
        values = []

        # while cursor is not null, traverse and add node value to values
        while cursor != None:
            values.append(cursor.val)
            cursor = cursor.next
        
        # sort values
        values.sort()

        # initialize index variable i to 0
        i = 0
        # reinitialize pointer cursor to head of linkedlist
        cursor = node

        # while cursor is not null, set cursor value to values[i], 
        # traverse and increment i by 1
        while cursor != None:
            cursor.val = values[i]
            cursor = cursor.next
            i += 1

        # return head of linkedlist
        return node