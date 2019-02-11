# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Note that an empty string is also considered valid.

# Example 1:
# Input: "()"
# Output: true

# Example 2:
# Input: "()[]{}"
# Output: true

# Example 3:
# Input: "(]"
# Output: false

# Example 4:
# Input: "([)]"
# Output: false

# Example 5:
# Input: "{[]}"
# Output: true


class Solution:
    def isValid(self, s: 'str') -> 'bool':
        if len(s) == 1:
            return False
        if len(s) == 0:
            return True
        
        stack = []
        d = {'[':']','{':'}','(':')'}
        for char in s:
            if char in d:
                stack.append(char)
            else:
                if not stack or d[stack.pop()] != char:
                    return False
        return not stack #if stack is empty, True if not, False
            
                

        

s = Solution()
print(s.isValid("(("))
