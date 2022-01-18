"""
BINARY SEARCH: BINARY CHECKS

Given a list of integers prices representing prices of cars for 
sale, and a budget k, return the maximum number of cars you can buy.

Constraints
n ≤ 200,000 where n is the length of prices

Example 1
Input: prices = [90, 30, 20, 40, 90], k = 95
Output: 3
Explanation: We can buy the cars with prices 30, 20, and 40.

Example 2
Input: prices = [60, 90, 55, 75], k = 50
Output: 0
Explanation: We cannot afford any of these cars.
"""

class Solution:
    def solve(self, prices, k):
        # sort array prices; this allows us to move from the
        # minimum price up to maximize the number of cars
        prices.sort()
        # initialize variable sump to store the sum of prices
        sump = 0
        # initialize index variable i
        i = 0

        # while i is less than the length of array prices
        while i < len(prices):
            # if the current sump + the price at index i is 
            # larger than our budget k, break the loop
            if sump + prices[i] > k:
                break
            # else, update the current sump
            sump += prices[i]
            # increment i
            i += 1
        
        # return i, the maximum number of cars we can buy while
        # staying in our budget
        return i