"""
BINARY SEARCH: UNIVALUE TREE

Given a binary tree root, return whether all values in the tree are the same.

Constraints
n ≤ 100,000 where n is the number of nodes in root

Example 1
Input: root = [2, [2, [2, null, null], null], [2, [2, null, null], null]]
Output: True
Explanation: Every node has the value 2

Example 2
Input: root = [2, [2, [9, null, null], null], [2, null, null]]
Output: False
Explanation: There is a node with a value 9 while others are 2
"""

class Tree:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def solvehelp(self, root, val):
        # if root is null, return True
        if root == None:
            return True
        # if current node value is not equal to passed value, return False
        if root.val != val:
            return False
        # else return recursive results of left and right subtree
        return self.solvehelp(root.left, val) and self.solvehelp(root.right, val)

    def solve(self, root):
        # if root is not null
        if root:
            # return result of helper method
            # this checks that every node value is equal to root.val
            return self.solvehelp(root, root.val)
        # if root is null, return true
        return True