"""
BINARY SEARCH: 123 NUMBER FLIP

You are given an integer n consisting of digits 1, 2, and 3 and 
you can flip one digit to a 3. Return the maximum number you can make.

Constraints
1 ≤ n < 2 ** 31

Example 1
Input: n = 123
Output: 323
Explanation: We flip 1 to 3

Example 2
Input: n = 333
Output: 333
Explanation: Flipping doesn't help.
"""

import re

class Solution:
    def solve(self, n):
        # replace leftmost non 3 digit with 3
        """
        num = str(n)
        maxnum = re.sub("[1-2]", "3", num, count=1)
        return int(maxnum)
        """
        return int(re.sub("[1-2]", "3", str(n), count=1))
