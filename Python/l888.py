# Alice and Bob have candy bars of different sizes: A[i] is the size of the i-th bar of candy that Alice has, 
# and B[j] is the size of the j-th bar of candy that Bob has.

# Since they are friends, they would like to exchange one candy bar each so that after the exchange, they both 
# have the same total amount of candy.  (The total amount of candy a person has is the sum of the sizes of candy bars they have.)

# Return an integer array ans where ans[0] is the size of the candy bar that Alice must exchange, and ans[1] is 
# the size of the candy bar that Bob must exchange.

# If there are multiple answers, you may return any one of them.  It is guaranteed an answer exists.

# Example 1:
# Input: A = [1, 1], B = [2, 2]
# Output: [1, 2]

# Example 2:
# Input: A = [1, 2], B = [2, 3]
# Output: [1, 2]

# Example 3:
# Input: A = [2], B = [1, 3]
# Output: [2, 3]

# Example 4:
# Input: A = [1, 2, 5], B = [2, 4]
# Output: [5, 4]


class Solution:
    def fairCandySwap(self, A: 'List[int]', B: 'List[int]') -> 'List[int]':
        #brute force O(n^2)
        # fair_amount = int((sum(A) + sum(B)) / 2)
        # for i in range(len(A)):
        #     for j in range(len(B)):
        #         if sum(B) - B[j] + A[i] == fair_amount:
        #             return [A[i], B[j]]
        # optimized O(n)
        if sum(A) > sum(B):
            small = sum(B)
            boo = 0
        else:
            small = sum(A)
            boo = 1
        fair_amount = int((sum(A) + sum(B)) / 2)
        difference = fair_amount - small
        if boo == 0:
            for i in range(len(B)):
                if B[i] + difference in A:
                    return [B[i] + difference, B[i]]
        else:
            for i in range(len(A)):
                if A[i] + difference in B:
                    return [A[i], A[i] + difference]
        


s = Solution()
print(s.fairCandySwap([1, 1],[2, 2]))
