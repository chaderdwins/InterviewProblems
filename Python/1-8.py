import unittest

# write an algorithm such that if an element in an MxN matrix is 0, its entire
# row and column are zero

def zero_matrix(mtx):
    boo = 0
    li = []
    i = 0
    j = 0
    while i < len(mtx):
        boo = 0
        while j < len(mtx[i]):
            if 0 in mtx[i]:
                boo = 1
            if mtx[i][j] == 0:
                if j not in li:
                    li.append(j)
            if boo == 1:
                mtx[i][j] = 0
            j += 1
        i += 1
        j = 0

    i = 0
    j = 0
    while i < len(mtx):
     while j < len(mtx[i]):
         if j in li:
             mtx[i][j] = 0
         j += 1
     i += 1
     j = 0
    return mtx

# unit testing
class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ([
            [1, 2, 3, 4, 0],
            [6, 0, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 0, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ], [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [11, 0, 13, 14, 0],
            [0, 0, 0, 0, 0],
            [21, 0, 23, 24, 0]
        ])
    ]

    def test_zero_matrix(self):
        for [test_matrix, expected] in self.data:
            actual = zero_matrix(test_matrix)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
