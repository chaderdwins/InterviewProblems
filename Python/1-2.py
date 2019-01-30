import unittest

#given two strings, write a method to see if they are permutations of one another

def check_permutation(st1, st2):
    if len(st1) != len(st2):
        return False
    a , b = {}, {}
    
    for char in st1:
        if char in a:
            a[char] +=1
        else:
            a[char] = 1

    for char in st2:
        if char in b:
            b[char] +=1
        else:
            b[char] = 1

    if a != b:
        return False
    return True

#unit testing
class Test(unittest.TestCase):
    dataT = (
        ('abcd', 'bacd'),
        ('3563476', '7334566'),
        ('wef34f', 'wffe34'),
    )
    dataF = (
        ('abcd', 'd2cba'),
        ('2354', '1234'),
        ('dcw4f', 'dcw5f'),
    )

    def test_cp(self):
        # true check
        for test_strings in self.dataT:
            result = check_permutation(*test_strings)
            self.assertTrue(result)
        # false check
        for test_strings in self.dataF:
            result = check_permutation(*test_strings)
            self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()
