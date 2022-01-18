"""
BINARY SEARCH: ELEPHANT TREE

Given a binary tree root, return the same tree except every node's 
value is replaced by its original value plus all of the sums of 
its left and right subtrees.

Constraints
n ≤ 100,000 where n is the number of nodes in root

Example 1
Input: root = [2, [1, [0, null, null], null], [4, [3, null, null], null]]
Output: [10, [1, [0, null, null], null], [7, [3, null, null], null]]
"""

class Tree:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def updatevals(self, root):
        # initialize treesum to 0
        treesum = 0

        # if the root is not null
        if root:
            # update values of left subtree
            # add this to the current treesum
            treesum += self.updatevals(root.left)
            # add current root value to treesum
            treesum += root.val
            # update values of right subtree
            # add this to the current treesum
            treesum += self.updatevals(root.right)
            # set the current root value to treesum
            # this updates the original tree
            root.val = treesum
        
        # return treesum
        return treesum

    def solve(self, root):
        # call updatevals to update the tree
        self.updatevals(root)
        # return the tree
        return root