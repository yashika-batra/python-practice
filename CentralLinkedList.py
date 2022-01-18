"""
BINARY SEARCH: CENTRAL LINKED LIST

Given a singly linked list node, return the value of the middle node. 
If there's two middle nodes, then return the second one.

Bonus: Solve using O(1) space.

Constraints
n ≤ 100,000 where n is the number of nodes in node

Example 1
Input: node = [0, 1, 2]
Output: 1
"""

class LLNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    def solve(self, node):
        # initialize a cursor to traverse the list
        cursor = node
        # initialize list length to 0
        length = 0

        # while cursor is not null, traverse and increment length
        while cursor:
            cursor = cursor.next
            length += 1

        # initialize index variable i to 0
        i = 0
        # reinitialize cursor to the start of the list
        cursor = node

        # while the current index is less than half the total length
        # of the list, traverse and increment the current index
        while i < length // 2:
            cursor = cursor.next
            i += 1

        # by the end of this while loop, the cursor is at the middle
        # of the linked list. return the value of the current node
        return cursor.val

