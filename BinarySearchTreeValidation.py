"""
BINARY SEARCH: BINARY SEARCH TREE VALIDATION

Given a binary tree root, return whether it's a binary search tree. 
A binary tree node is a binary search tree if :
All nodes on its left subtree are smaller than node.val
All nodes on its right subtree are bigger than node.val
All nodes hold the these properties.

Constraint
n ≤ 100,000 where n is the number of nodes in root

Example 1
Input: root = [3, [2, null, null], [9, [7, [4, null, null], 
[8, null, null]], [12, null, null]]]
Output: True
Example 2
Input: root = [3, [1, null, null], [5, [4, null, [7, null, null]], 
[6, null, null]]]
Output: False
Explanation: This is not a binary search tree because the 7 is 
not smaller than 5.
"""

class Tree:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def solvehelp(self, root, lowval, highval):
        # base case
        if root == None:
            return True

        # if lower bound is less than the current root value
        # and the upperbound is greater than the current root value
        # for all subtree roots in the tree, return true
        return (lowval < root.val and highval > root.val and 
            # recursively check the left subtree
            # upper bound / highval is the current root value
            # for a valid binary search tree
            self.solvehelp(root.left, lowval, root.val) and 
            # recursively check the right subtree
            # lower bound / lowval is the current root value
            # for a valid binary search tree
            self.solvehelp(root.right, root.val, highval))
    
    def solve(self, root):
        # call helper function
        # lowval = -inf, highval = inf originally
        return self.solvehelp(root, float("-inf"), float("inf"))