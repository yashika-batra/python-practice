"""
BINARY SEARCH: TREE SUM

Given a binary tree root, return the sum of all values in the tree.

Constraints
n ≤ 100,000 where n is the number of nodes in root

Example 1
Input: root = [1, [2, null, null], [3, [5, null, null], null]]
Output: 11
Explanation: 11 = 1 + 2 + 3 + 5

Example 2
Input: root = [1, [2, [3, null, null], null], null]
Output: 6
Explanation: 6 = 1 + 2 + 3
"""

class Tree:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def solve(self, root):
        # initialize treesum to 0
        treesum = 0

        # if root is not null
        if root:
            # recursively add sum of left subtree to treesum
            treesum += self.solve(root.left)
            # add value of current node to treesum
            treesum += root.val
            # recursively add sum of right subtree to treesum
            treesum += self.solve(root.right)
        
        # return treesum
        return treesum
        