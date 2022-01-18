"""
BINARY SEARCH: COUNT BST NODES IN A RANGE

Given a binary search tree root, and integers lo and hi, 
return the count of all nodes in root whose values are 
between [lo, hi] (inclusive).

Constraints
n ≤ 100,000 where n is the number of nodes in root

Example 1
Input: root = [3, [2, null, null], [9, [7, [4, null, null], [8, null, null]], [12, null, null]]]. 
lo = 5, hi = 10
Output: 3
Explanation: Only 7, 8, 9 are between [5, 10].
"""

class Tree:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def solve(self, root, lo, hi):
        # base case, if root is null, add 0 to the total number of nodes
        if root == None:
            return 0
        elif root.val <= hi and root.val >= lo:
            # if root is in range, look at left and right subtrees
            # add 1 to account for the current root
            return 1 + self.solve(root.left, lo, hi) + self.solve(root.right, lo, hi)
        elif root.val > hi:
            # if root outside upper end of range, look at values smaller than root (left)
            return self.solve(root.left, lo, hi)
        elif root.val < lo:
            # if root outside lower end of range, look at values larger than root (right)
            return self.solve(root.right, lo, hi)