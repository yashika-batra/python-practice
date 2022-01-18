"""
BINARY SEARCH: PALINDROMIC ANAGRAM

Given a string s, determine whether any anagram of s is a palindrome.

Constraints
n ≤ 100,000 where n is the length of s

Example
Input: s = "carrace"
Output: True
Explanation: "carrace" should return true, since it can be rearranged to 
form "racecar", which is a palindrome.
"""

class Solution:
    def solve(self, s):
        # Any palindromic string must have each character an even number of times
        # However, it may have 1 character an odd number of times
        # Ex. racecar has 'r', 'a', 'c', 3 times, and 'e' 1 time
        # Ex. sees has 's' and 'e' 2 times each
        # For an anagram of s to possibly be a palindrome, it must follow the same
        # pattern

        # initialize oddcharcount to 0
        oddcharcount = 0
        # initialize a dictionary chardict
        chardict = dict()

        # for each character in string s
        for ch in s:
            # if ch is already in the dictionary, increment chardict[ch] by 1
            if ch in chardict:
                chardict[ch] += 1
            # else initialize chardict[ch] to 1
            else:
                chardict[ch] = 1
        
        # for each character in the dictionary
        for ch in chardict:
            # if ch appears an odd number of times, increment oddcharcount by 1
            if chardict[ch] % 2 == 1:
                oddcharcount += 1
            # if oddcharcount is greater than 1, return False
            if oddcharcount > 1:
                return False
        # return True
        return True