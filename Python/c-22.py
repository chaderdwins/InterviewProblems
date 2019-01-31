# <p>Write a function called <strong>find_the_duplicate</strong> which accepts an
#  array of numbers containing a single duplicate. The function returns the number
#  which is a duplicate or None if there are no duplicates.</p>

'''
find_the_duplicate([1,2,1,4,3,12]) # 1
find_the_duplicate([6,1,9,5,3,4,9]) # 9
find_the_duplicate([2,1,3,4]) # None
'''

def find_the_duplicate(li):
    li.sort()
    for item in range(len(li)):
        try:
            if li[item] == li[item+1]:
                return li[item]
        except IndexError:
            return None


print(find_the_duplicate([1,2,1,4,3,12]))
