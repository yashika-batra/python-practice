"""
BINARY SEARCH: PARTITION TREE

Given the root to a binary tree root, return a list of two numbers 
where the first number is the number of leaves in the tree and 
the second number is the number of internal (non-leaf) nodes.

Constraints
n ≤ 100,000 where n is the number of nodes in root

Example 1
Input: root = [1, [5, null, null], [3, null, null]]
Output: [2, 1]
Explanation: This tree has 2 leaves and 1 internal node.
"""

class Tree:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def solvehelp(self, root, leafnodearr, totalnodearr):
        # if root is not null
        if root:
            # recursively look at left subtree
            self.solvehelp(root.left, leafnodearr, totalnodearr)
            # if no left or right subtree, current node is a leaf node
            # append current node value to leafnodearr
            if root.left == None and root.right == None:
                leafnodearr.append(root.val)
            # append current node value to totalnodearr
            totalnodearr.append(root.val)
            # recursively look at right subtree
            self.solvehelp(root.right, leafnodearr, totalnodearr)
        # return leafnodearr and totalnodearr
        # leadnodearr contains all leaf node values
        # totalnodearr contains all node values
        return leafnodearr, totalnodearr

    def solve(self, root):
        # call helper function to find arr of leaf nodes and arr of total nodes
        leafnodearr, totalnodearr = self.solvehelp(root, [], [])
        # leafnodes and totalnodes are equal to the length of the respective arrs
        leafnodes, totalnodes = len(leafnodearr), len(totalnodearr)
        # return an array containing leafnodes and totalnodes - leafnodes
        # totalnodes - leafnodes is equal to the number of internal nodes
        return [leafnodes, totalnodes - leafnodes]