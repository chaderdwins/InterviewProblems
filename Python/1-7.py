import unittest

# given an image represented by a NxN matrix, where each pixel in the image is 4 bytes,
# write a fxn to rotate the matrix by 90 degrees. Can you do this in place?

def rotate_matrix(mtx):
    mtx = mtx[::-1] #step one is to reverse the matrix
    print(mtx)
    new_mtx = list(zip(*mtx)) #using argument unpacking to pass the contents to zip
    i = 0
    while i < len(new_mtx): #zip returns a tuple, so we need to convert each item to a list
        new_mtx[i] = list(new_mtx[i])
        i += 1
    # print(new_mtx)
    return new_mtx

# unit testing
class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ([
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ], [
            [21, 16, 11, 6, 1],
            [22, 17, 12, 7, 2],
            [23, 18, 13, 8, 3],
            [24, 19, 14, 9, 4],
            [25, 20, 15, 10, 5]
        ])
    ]

    def test_rotate_matrix(self):
        for [test_matrix, expected] in self.data:
            actual = rotate_matrix(test_matrix)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
