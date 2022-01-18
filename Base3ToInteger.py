"""
BINARY SEARCH: BASE 3 TO INTEGER

Given a string s representing a number in base 3 (consisting only 
of 0, 1, or 2), return its decimal integer equivalent. This should 
be implemented directly without using a built-in function.

Example 1
Input: s = "10"
Output: 3

Example 2
Input: s = "21"
Output: 7
"""

class Solution:
    def solve(self, s):
        # initialize snum to an integer version of s
        # ex. "123" --> 123
        snum = int(s)
        # initialize variable sol to 0. this will hold the decimal
        # representation of s
        sol = 0
        # initialize variable digit. this will store the current
        # digit place
        digit = 0
        
        # while snum is greater than 0, add the one's place of snum 
        # times 3^digit to sol
        while snum > 0:
            sol += (3 ** digit) * (snum % 10)
            # divide snum by 10; this looks at the next one's place
            # even though snum is base 3, we stored it as an integer
            # this means that it is by default stored as "decimal"
            snum = snum // 10
            # increment digit
            digit += 1

        # return sol
        return sol