"""
BINARY SEARCH: ANAGRAM CHECKS

Given two strings s0 and s1, return whether they are anagrams of 
each other.

Constraints
n ≤ 100,000 where n is the length of s0
m ≤ 100,000 where m is the length of s1

Example 1
Input: s0 = "listen", s1 = "silent"
Output: True

Example 2
Input: s0 = "bedroom", s1 = "bathroom"
Output: False
"""

class Solution:
    def solve(self, s0, s1):
        # initialize dictionaries to store character counts for s0 and s1
        s0dict = dict()
        s1dict = dict()

        # for every character in s0
        for s in s0:
            # if key s is in s0dict, increment count
            if s in s0dict:
                s0dict[s] += 1
            # else initialize count to 1
            else:
                s0dict[s] = 1

        # for every character in s1
        for s in s1:
            # if key s is in s1dict, increment count
            if s in s1dict:
                s1dict[s] += 1
            # else initialize count to 1
            else:
                s1dict[s] = 1

        # if dictionaries are equal, return True
        # else return False
        return s0dict == s1dict

        