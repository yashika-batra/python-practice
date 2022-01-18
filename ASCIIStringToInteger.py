"""
BINARY SEARCH: ASCII STRING TO INTEGER

You are given a string s containing digits from "0" to "9" and 
lowercase alphabet characters. Return the sum of the numbers 
found in s.

Constraints
1 ≤ n ≤ 100,000 where n is the length of s

Example 1
Input: s = "11aa32bbb5"
Output: 48
Explanation: Since 11 + 32 + 5 = 48.

Example 2
Input: s = "abc"
Output: 0
Explanation: There's no digits so it defaults to 0.

Example 3
Input: s = "1a2b30"
Output: 33
Explanation: Since 1 + 2 + 30 = 33.
"""

import re 

class Solution:
    def solve(self, s):
        # split s into an array of characters using lowercase
        # character substrings as regex
        sarray = re.split('[a-z]+', s)
        # initialize s_sum to 0; this will hold the sum of the numbers in s
        s_sum = 0

        # for every numerical substring n in sarray
        for n in sarray:
            # if n is not empty, add the integer value of n to s_sum
            if n != "":
                s_sum += int(n)

        # return s_sum
        return s_sum
