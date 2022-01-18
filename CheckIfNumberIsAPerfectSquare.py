"""
BINARY SEARCH: CHECK IF NUMBER IS A PERFECT SQUARE

Given an integer n, return whether n = k * k for some integer k.
This should be done without using built-in square root function.

Constraints
0 ≤ n < 2 ** 31

Example 1
Input: n = 25
Output: True
Explanation: 25 = 5 * 5
"""

class Solution:
    def solve(self, n):
        # uses a binary search to find the integer square root of n.
        # if root is found, returns True, else returns False

        # if n is 0 or 1, return true
        if n == 0 or n == 1:
            return True
        
        # initialize variable lo to 0
        lo = 0
        # initialize variable hi to integer n/2 + 1
        # the integer square root of perfect square can never be larger than
        # 1/2 the perfect square for all perfect squares >= 4
        hi = n // 2 + 1

        # while lo < hi
        while lo < hi:
            # variable mid is equal to the average of lo and hi
            mid = lo + (hi - lo) // 2

            # if mid^2 = n, there exists an integer square root of n,
            # return True
            if mid ** 2 == n:
                return True
            # if mid^2 > n, we can lower our hi bound to mid
            elif mid ** 2 > n:
                hi = mid
            # else, mid^2 < n, we can increase our lo bound to mid + 1
            else:
                lo = mid + 1
        
        # at the end of this loop, lo = hi and we have found no
        # integer square root. therefore, no integer square root exists,
        # and we return False
        return False

