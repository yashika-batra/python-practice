"""
BINARY SEARCH: ARITHMETIC SEQUENCE PERMUTATION

Given a list of integers nums, return whether you can rearrange 
the order of nums such that the difference between every 
consecutive two numbers is the same.

Constraints
n ≤ 100,000 where n is the length of nums

Example 1
Input: nums = [7, 1, 5, 3]
Output: True
Explanation: If we rearrange nums to [1, 3, 5, 7], then the difference between 
every two consecutive numbers is 2.

Example 2
Input: nums = [1, 5, 1, 5, 1, 5]
Output: False
Explanation: The difference between every consecutive two numbers alternates 
between 4 and -4.
"""

class Solution:
    def solve(self, nums):
        # if nums has size 0 or 1, return True
        if len(nums) == 0 or len(nums) == 1:
            return True
        
        # sort nums
        nums.sort()
        # initialize difference to the difference between 
        # the first two consecutive numbers in nums
        difference = nums[1] - nums[0]

        # for every other value in sorted nums
        for i in range(2, len(nums)):
            # if the difference between two consecutive numbers
            # is not difference, return False
            if nums[i] - nums[i - 1] != difference:
                return False

        # if we have not already returned False, every set of consecutive
        # numbers in nums has the same difference, return True
        return True