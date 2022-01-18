"""
BINARY SEARCH: LEVEL ORDER ALTERNATING

Given a binary tree root, return values of the nodes in each level, 
alternating from going left-to-right and right-to-left.

Constraints
n ≤ 100,000 where n is the number of nodes in root

Example 1
Input: root = [3, [0, null, [2, [1, null, null], null]], [4, null, null]]
Output: [3, 4, 0, 2, 1]
"""

class Tree:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getheight(self, root):
        # if root is null, return 0
        if root == None:
            return 0
        # find left subtree height and right subtree height recursively
        leftheight = self.getheight(root.left)
        rightheight = self.getheight(root.right)
        # return maximum of both subtree heights + 1
        # + 1 accounts for the added level of the current node
        return max(leftheight, rightheight) + 1

    def solveleft(self, root, h, sol):
        # if root is null, return nothing
        if root == None:
            return

        # if height is 1, append the root value
        if h == 1:
            sol.append(root.val)

        # if height is greater than 1
        if h > 1:
            # recursively look at left subtree (decrease height by 1)
            self.solveleft(root.left, h - 1, sol)
            # recursively look at right subtree (decrease height by 1)
            self.solveleft(root.right, h - 1, sol)

    def solveright(self, root, h, sol):
        # if root is null, return nothing
        if root == None:
            return

        # if height is 1, append the root value
        if h == 1:
            sol.append(root.val)

        # if height is greater than 1
        if h > 1:
            # recursively look at left subtree (decrease height by 1)
            self.solveright(root.right, h - 1, sol)
            # recursively look at right subtree (decrease height by 1)
            self.solveright(root.left, h - 1, sol)
        
    def solve(self, root):
        # find total height of the tree
        level = self.getheight(root)
        # initialize sol, array to store result
        sol = []
        # initialize index h to 0
        h = 0

        # traverse the levels of the tree using h
        while h < level + 1:
            # if h is odd, append values on current level left to right
            if h % 2 == 1:
                self.solveleft(root, h, sol)
                h += 1
            # if h is even, append values on current level right to left
            else:
                self.solveright(root, h, sol)
                h += 1
        
        # return sol, which contains node values in level alternating order
        return sol