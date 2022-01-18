"""
BINARY SEARCH: LEAF EQUIVALENT TREES

Given two binary trees root0 and root1, return whether the 
sequence of leaves left-to-right in both trees are the same.

Constraints
n ≤ 100,000 where n is the number of nodes in root0
m ≤ 100,000 where m is the number of nodes in root1

Example 1
Input: 
root0 = [0, [3, null, [2, null, null]], [1, [1, null, null], null]]
root1 = [0, [1, null, [2, null, null]], [3, null, [1, null, null]]]
Output: True
Explanation: Both trees have leaves [2, 1].

Example 2
Input:
root0 = [1, [2, null, null], [3, null, null]]
root1 = [1, [3, null, null], [2, null, null]]
Output: False
Explanation: The left tree has [2, 3] and right has [3, 2]
"""

class Tree:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution:
    def leafarrhelp(self, root, arr):
        # if root is not null
        if root:
            # recursively call leafarrhelp on left subtree
            self.leafarrhelp(root.left, arr)
            # if current node has no left or right subtree,
            # it is a leaf node. append this node's value
            # to arr
            if root.left == None and root.right == None:
                arr.append(root.val)
            # recursively call leafarrhelp on right subtree
            self.leafarrhelp(root.right, arr)
        # return arr, which contains values of leaf nodes of tree root
        return arr

    def leafarr(self, root):
        # return result arr of helper method
        return self.leafarrhelp(root, [])

    def solve(self, root0, root1):
        # if the arr of leaf nodes of tree root0 is equal
        # to the arr of lead nodes of tree root1, return true
        # else return false
        return self.leafarr(root0) == self.leafarr(root1)