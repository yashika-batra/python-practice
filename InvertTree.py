"""
BINARY SEARCH: INVERT TREE

Given a binary tree root, invert it so that its left subtree and right 
subtree are swapped and the children are recursively inverted.

Constraints
n ≤ 100,000 where n is the number of nodes in root

Example 1
Input: root = [0, [2, null, null], [9, [7, null, null], [12, null, null]]]
Output: [0, [9, [12, null, null], [7, null, null]], [2, null, null]]
"""

class Tree:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def solve(self, root):
        # if root is null, do nothing
        if root == None:
            return
        
        # recursive call on left subtree
        self.solve(root.left)
        # recursive call on right subtree
        self.solve(root.right)

        # swap pointers to left and right subtrees
        temp = root.left
        root.left = root.right
        root.right = temp

        # return root node of binary tree
        return root
