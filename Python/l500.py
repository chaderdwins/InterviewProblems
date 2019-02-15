# Given a List of words, return the words that can be typed using 
# letters of alphabet on only one row's of American keyboard like the image below.

# Example:
# Input: ["Hello", "Alaska", "Dad", "Peace"]
# Output: ["Alaska", "Dad"]


class Solution:
    def findWords(self, words: 'List[str]') -> 'List[str]':
        row1 = set('QWERTYUIOPqwertyuiop')
        row2 = set('ASDFGHJKLasdfghjkl')
        row3 = set('ZXCVBNMzxcvbnm')
        #we test if every element in set(word) is in row1, row2, or row3
        return [word for word in words if set(word)<=row1 or set(word)<=row2 or set(word)<=row3]
    

s = Solution()
print(s.findWords(["Hello", "Alaska", "Dad", "Peace"]))
