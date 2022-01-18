"""
BINARY SEARCH: SUBMAJORITY VOTE

You are given a list of integers nums where each number represents a vote to a candidate.
Return the ids of the candidates that have greater than floor(n/3) votes, in ascending order.

Bonus: solve in O(1) space.

Constraints
n ≤ 100,000 where n is the length of nums.

Example 1
Input: nums = [2, 1, 5, 5, 5, 5, 6, 6, 6, 6, 6]
Output: [5, 6]
Explanation: Both 5 and 6 have 40% of the votes.

Example 2
Input: nums = [1, 1, 1, 1, 2, 3]
Output: [1]
"""

class Solution:
    def solve(self, nums):
        # number of votes necessary to qualify a candidate
        # is 1/3 of the total number of votes
        necessaryVote = len(nums) // 3

        # initialize dictionary voteDict
        voteDict = dict()
        # initlaize solution array sol
        sol = []

        # loop through every vote
        for n in nums:
            # if candidate is already in voteDict, increment
            # voteDict[n] by 1
            if n in voteDict:
                voteDict[n] += 1
            # else initialize voteDict[n] to 1
            else:
                voteDict[n] = 1
        
        # loop through every candidate in voteDict
        for candidate in voteDict:
            # if candidate has more votes than necessaryVote
            # add candidate to solution arr
            if voteDict[candidate] > necessaryVote:
                sol.append(candidate)

        # sort solution array and return 
        sol.sort()
        return sol