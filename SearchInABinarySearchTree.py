"""
BINARY SEARCH: SEARCH IN A BINARY SEARCH TREE

Given a binary search tree root and an integer val, determine whether val is in the tree.

Constraints
n ≤ 100,000 where n is the number of nodes in root

Example 1
Input: root = [3, [2, null, null], [9, [7, [4, null, null], [8, null, null]], [12, null, null]]], 
val = 4
Output: True

Example 2
Input: root = [3, [2, null, null], [9, [7, [4, null, null], [8, null, null]], [12, null, null]]], 
val = 100
Output: False
"""

class Tree:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def solve(self, root, val):
        # if root is null, return False
        if root == None:
            return False
        # if the current value is equal to the target value, return True
        if root.val == val:
            return True
        # if the current value is greater than target value, recursively 
        # search the right subtree
        if val > root.val:
            return self.solve(root.right, val)
        # if the current value is less than target value, recursively
        # search the left subtree
        elif val < root.val:
            return self.solve(root.left, val)