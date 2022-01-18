"""
BINARY SEARCH: VERTICAL WORD ARRANGEMENT

You are given a string s containing lowercase alphabet characters 
separated by spaces " ". After splitting the string on spaces, 
return all the words in vertical order, top to bottom. If there's no 
character on a column, use a space.

Constraints
1 ≤ n ≤ 1,000 where n is the length of s

Example 1
Input: s = "abc def ghij"
Output: ["adg", "beh", "cfi", "  j"]
Explanation: After splitting the string we get ["abc", "def", "ghij"]
Then, traversing vertically we can group them into "adg", "beh", "cfi", "   j".
"""

class Solution:
    def solve(self, s):
        # split string into array of words using delimeter ""
        stringarr = s.split(" ")
        # initialize matrix
        matrix = []
        # initialize variable row to 0, maxlength to 0
        row = 0
        maxlength = 0

        # loop through every string in stringarr
        for string in stringarr:
            # add a new row to matrix
            matrix.append([])
            
            # for every character in the current string
            for c in string:
                # add character to the current matrixr row
                matrix[row].append(c)

            # maxlength is the max of current maxlength and length of current row
            maxlength = max(maxlength, len(matrix[row]))
            # increment row number by 1
            row += 1
        
        # for every row in matrix
        for row in matrix:
            # if the length of row is less than maxlength, append " " to the row
            # until its length is equal to maxlength
            while len(row) < maxlength:
                row.append(" ")

        # initialize array result to store vertical words from matrix
        result = []
        
        # for every column in matrix
        for c in range(len(matrix[0])):
            # initialize empty string
            string = ""

            # for every row in matrix
            for r in range(len(matrix)):
                # add one character at a time to string, 
                # move down the columns
                string += matrix[r][c]
            
            # strip whitespace from the right end of the string
            # Ex. " abc" --> " abc", but "abc " --> "abc"
            # we do not want space after the end of the word
            string = string.rstrip()
            # add each column's string to result array
            result.append(string)

        # return result array
        return result