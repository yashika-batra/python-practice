"""
BINARY SEARCH: A STRICTLY INCREASING LINKED LIST

Given the head of a singly linked list head, return whether the 
values of the nodes are sorted in a strictly increasing order.

Constraints
1 ≤ n ≤ 100,000 where n is the number of nodes in head

Example 1
Input: head = [1, 5, 9, 9]
Output: False
Explanation: Even though this list is sorted, it's not strictly 
increasing since 9 is repeated.

Example 2
Input: head = [1, 5, 8, 9]
Output: True
Explanation: The values 1, 5, 8, 9 are strictly increasing.
"""

class LLNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    def solve(self, head):
        # initialize cursor pointer to point to head node
        cursor = head

        # while cursor.next is not null
        while cursor.next != None:
            # if the current node's value is greater than or equal
            # to the next nodes value, the linkedlist is not 
            # strictly increasing, return False
            if cursor.val >= cursor.next.val:
                return False
            # traverse forward
            cursor = cursor.next
        
        # if we have not already returned False, this means the linkedlist
        # is strictly increasing, return True
        return True