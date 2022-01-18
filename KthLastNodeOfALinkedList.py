"""
BINARY SEARCH: KTH LAST NODE OF A LINKED LIST

Given a singly linked list node, return the value of the kth last node 
(0-indexed). k is guaranteed not to be larger than the size of the linked list.

This should be done in O(1) space.

Constraints
n ≤ 100,000 where n is the length of node

Example 1
Input: node = [1, 2], k = 1
Output: 1
Explanation: The second last node has the val of 1

Example 2
Input: node = [0, 1, 2, 3], k = 2
Output: 1
"""

class LLNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    def solve(self, node, k):
        # initialize cursor variable to front of list
        cursor = node
        # initialize length variable to 0
        length = 0

        # while cursor is not null, traverse and increment length
        while cursor:
            cursor = cursor.next
            length += 1
        
        # initialize index variable i to 0
        i = 0
        # reinitialize cursor variable to front of list
        cursor = node

        # while index is less than length - k - 1, traverse and increment i
        while i < length - k - 1:
            cursor = cursor.next
            i += 1

        # by the end of this loop, we would have reached the kth last node
        # of the list. return the value of this node
        return cursor.val

