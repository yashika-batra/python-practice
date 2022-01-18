"""
BINARY SEARCH: REVERSE A LINKED LIST

Given a singly linked list node, return its reverse.
Bonus: Can you do this in O(1) space?

Constraints
n ≤ 100,000 where n is the number of nodes in node

Example 1
Input: node = [1, 2, 3, 4]
Output: [4, 3, 2, 1]

Example 2
Input: node = [0, 1]
Output: [1, 0]
"""

class LLNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    def solve(self, node):
        # initialize pointer previous to null 
        previous = None
        # initialize pointer current to head of list
        current = node

        while current:
            # store next node in pointer nextnode
            nextnode = current.next
            # reverse current.next pointer to previous
            current.next = previous
            # iterate forward, previous points to current and 
            # current points to nextnode
            previous = current
            current = nextnode
        # set node to previous (new head of the list)
        node = previous

        # return node
        return node

