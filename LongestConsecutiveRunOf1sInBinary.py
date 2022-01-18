"""
BINARY SEARCH: LONGEST CONSECUTIVE RUN OF 1S IN BINARY

Given a non-negative integer n, return the length of the longest 
consecutive run of 1s in its binary representation.

Constraints
0 ≤ n < 2 ** 31

Example 1
Input: n = 156
Output: 3
Explanation: 156 is10011100 in binary and there's a run of length 3.
"""

class Solution:
    def solve(self, n):
        # initialize binaryn to the string of the binary form of n
        binaryn = str(bin(n))
        # initialize variable max1s to 0
        max1s = 0
        # initialize variable num1s, which holds the number of consecutive
        # 1s at a time, to 0
        num1s = 0

        for b in binaryn:
            # if b = 1, increment num1s
            if b == '1':
                num1s += 1
            # if b = 0, reset num1s to 0
            else:
                num1s = 0
            # max1s is the maximum of current max1s and num1s
            # max1s now holds the maximum number of consecutive 1s at a time
            max1s = max(max1s, num1s)
        
        # return max1s
        return max1s