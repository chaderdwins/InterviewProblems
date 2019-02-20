class Solution:
    def merge(self, nums1: 'List[int]', m: 'int', nums2: 'List[int]', n: 'int') -> 'None':
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m > 0 and n > 0:
            while len(nums1) > m:
                nums1.pop()
            nums1.extend(nums2)
            nums1.sort()
        elif m > 0 and n < 1:
            pass
        elif m < 1 and n >= 1:
            while nums1:
                nums1.pop()
            nums1.extend(nums2)
            nums1.sort()

           
        