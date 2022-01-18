"""
BINARY SEARCH: 3-6-9

Given an integer n, return a list with each number from 1 to n, 
except if it's a multiple of 3 or has a 3, 6, or 9 in the number, 
it should be the string "clap".

Note: return the number as a string.

Constraints
n ≤ 100,000

Example 1
Input: n = 16
Output: ["1", "2", "clap", "4", "5", "clap", "7", "8", "clap", "10", "11", "clap", "clap", 
"14", "clap", "clap"]
Explanation: 
3, 6, 9, 12, and 15 are replaced by "clap" since they are divisible by 3.
13 is replaced since it has a 3 in the number.
16 is replaced since it has a 6 in the number.
"""

class Solution:
    def solve(self, n):
        # initialize array sol
        sol = []

        # for i in inclusive range, [1, n]
        for i in range(1, n + 1):
            # if i is a multiple of 3, add "clap" to sol
            if i % 3 == 0:
                sol.append("clap")
            # if i contains the digit 3, 6, or 9, add "clap" to sol
            elif '3' in str(i) or '6' in str(i) or '9' in str(i):
                sol.append("clap")
            # else add i in string form
            else:
                sol.append(str(i))
        
        # return array sol
        return sol
