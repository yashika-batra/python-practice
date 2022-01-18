"""
BINARY SEARCH: INORDER TRAVERSAL

Given a binary tree root, return an inorder traversal of root as a list.
Bonus: Can you do this iteratively?

Constraints
n ≤ 100,000 where n is the number of nodes in root

Example
Input: root = [1, null, [159, [80, null, null], null]]
Output: [1, 80, 159]
"""

class Tree:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def solvehelp(self, root, arr):
        # if root is not null, update arr
        if root:
            # recursive call on left subtree
            self.solvehelp(root.left, arr)
            # append the current root value
            arr.append(root.val)
            # recursive call on right subtree
            self.solvehelp(root.right, arr)
        
        # return arr, contains node values from inorder traversal
        return arr

    def solve(self, root):
        # return the result of the helper function
        return self.solvehelp(root, [])

    """
    # inorder traversal iteratively
    def solve(self, root):
        # initialize arr to hold node values from inorder traversal
        arr = []
        # initialize stack
        stack = []
        # initialize current pointer to the root
        current = root

        # loop
        while True:
            # if current is not null, add current to stack, traverse left
            if current:
                stack.append(current)
                current = current.left

            # if current is null and the stack is not empty, 
            # pop the top node in the stack, and append its value to arr
            # update current to be equal to the right subtree of the popped node
            elif not current and len(stack) > 0:
                top = stack.pop()
                arr.append(top.val)
                current = top.right
        
            # if current is null and stack is empty, break loop
            else:
                break
        
        # return arr, contains node values from inorder traversal
        return arr
        """