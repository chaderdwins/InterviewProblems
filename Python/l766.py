# A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same element.
# Now given an M x N matrix, return True if and only if the matrix is Toeplitz.

# Example 1:
# Input:
# matrix = [
#     [1, 2, 3, 4],
#     [5, 1, 2, 3],
#     [9, 5, 1, 2]
# ]
# Output: True
# Explanation:
# In the above grid, the diagonals are:
# "[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]".
# In each diagonal all elements are the same, so the answer is True.

# Example 2:
# Input:
# matrix = [
#     [1, 2],
#     [2, 2]
# ]
# Output: False
# Explanation:
# The diagonal "[1, 2]" has different elements.


class Solution:
    def isToeplitzMatrix(self, matrix: 'List[List[int]]') -> 'bool':
        if len(matrix[0]) == 1:
            return True
        count = 1
        compare = matrix[0][:len(matrix[0])-1]
        while count < len(matrix):
            if compare != matrix[count][1:]:
                return False
            compare = matrix[count][:len(matrix[0])-1]
            count += 1
        return True          



# matrix = [
#     [1, 2, 3, 4],
#     [5, 1, 2, 3],
#     [9, 5, 1, 2]
# ]

matrix = [[11, 74, 7, 93], [40, 11, 74, 7]]
# matrix = [[1],[1]]
s = Solution()
print(s.isToeplitzMatrix(matrix))
