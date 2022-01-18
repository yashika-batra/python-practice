"""
BINARY SEARCH: EARLIEST UNIQUES IN A STREAM

Implement a data structure with the following methods:

EarliestUnique(int[] nums) constructs a new instance with the 
given list of numbers.
add(int num) adds num to the data structure.
firstUnique() returns the first unique number. If there's no 
unique number, return -1.

Constraints
n ≤ 100,000 where n is the number of calls to add and firstUnique.

Example 1
Input: methods = ["constructor", "add", "earliestUnique", "add", 
"earliestUnique"], arguments = [[[1, 2, 3]], [1], [], [2], []]`
Output: [None, None, 2, None, 3]
Explanation:
e = EarliestUnique([1, 2, 3])
e.add(1)
e.earliestUnique() == 2
e.add(2)
e.earliestUnique() == 3
"""

class EarliestUnique:
    def __init__(self, nums):
        # initialize a dictionary
        numsdict = dict()

        # fill dictionary based on values in nums
        for n in nums:
            # if n is already in numsdict, increment count
            if n in numsdict:
                numsdict[n] += 1
            # else initialize numsdict[num] to 1
            else:
                numsdict[n] = 1

        # initialize EarliestUnique object with
        # given nums as well as numsdict
        self.nums = nums
        self.numsdict = numsdict
        
    def add(self, num):
        # if num is already in numsdict, increment count
        if num in self.numsdict:
            self.numsdict[num] += 1
        # else initialize numsdict[num] to 1
        else:
            self.numsdict[num] = 1
        
    def earliestUnique(self):
        # loop through numsdict
        for num in self.numsdict:
            # if count of num is 1, it is a unique value in nums
            if self.numsdict[num] == 1:
                # return the first such instance
                return num
        # if no uniques, return -1
        return -1
        