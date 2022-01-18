"""
BINARY SEARCH: UNIQUE OCCURRENCES

Given a list of integers nums, return whether the number of 
occurrences of every value in the array is unique.
Note: Numbers can be negative.

Constraints
0 ≤ n ≤ 100,000 where n is the length of nums

Example:
Input: nums = [5, 3, 1, 8, 3, 1, 1, 8, 8, 8]
Output: True
Explanation: There's 1 occurrence of 5, 2 occurrences of 3, 3 occurrences of 1, 
and 4 occurrences of 8. All number of occurrences are unique.
"""

class Solution:
    def solve(self, nums):
        # initialize dictionary numdict
        numdict = dict()

        # for every number in nums
        for n in nums:
            # if n is already in numdict, increment count by 1
            if n in numdict:
                numdict[n] += 1
            # else initialize count to 1
            else:
                numdict[n] = 1

        # initialize set countset to hold the count values in numdict 
        countset = set()

        # for every key in numdict
        for key in numdict:
            # if the count of a given key is already in countset, return False
            # this means that the same count has shown up multiple times
            if numdict[key] in countset:
                return False
            # add count of key to countset
            countset.add(numdict[key])
        
        # if no key in numdict has a duplicate count, return True
        return True
