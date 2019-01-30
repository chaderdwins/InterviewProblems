import unittest

# given a string, write a function to check if it is a permutation of a palindrome.
def pal_perm(st):
    st = st.replace(' ', '').lower()
    di = {}
    for item in st:
        if item in di:
            di[item] += 1
        else:
            di[item] = 1

    count = 0
    for val in di.values():
        if count > 1:
            return False
        if val % 2 != 0:
            count += 1
    return True


#unit testing
class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('Tact Coa', True),
        ('jhsabckuj ahjsbckj', True),
        ('Able was I ere I saw Elba', True),
        ('So patient a nurse to nurse a patient so', False),
        ('Random Words', False),
        ('Not a Palindrome', False),
        ('no x in nixon', True),
        ('azAZ', True)]

    def test_pal_perm(self):
        for [test_string, expected] in self.data:
            actual = pal_perm(test_string)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
