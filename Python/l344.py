# Write a function that reverses a string. The input string is 
# given as an array of characters char[].

# Do not allocate extra space for another array, 
# you must do this by modifying the input array in-place with O(1) extra memory.

# You may assume all the characters consist of printable ascii characters.

# Example 1:
# Input: ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]

# Example 2:
# Input: ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]
class Solution:
    def reverseString(self, s: 'List[str]') -> 'None':
        x, y = 0, len(s)-1
        if len(s) % 2 == 0:
            while x != len(s) / 2:
                s[x], s[y] = s[y], s[x]
                x += 1
                y -= 1
        else:
            while x != y:
                s[x], s[y] = s[y], s[x]
                x += 1
                y -= 1
        return s

s = Solution()
print(s.reverseString(["h","e","l","l"]))