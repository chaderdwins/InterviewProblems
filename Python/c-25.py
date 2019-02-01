# Write a function called find_greater_numbers which accepts
# a list and returns the number of times a number is followed by a larger
# number across the entire list.
'''
find_greater_numbers([1,2,3]) # 3
find_greater_numbers([6,1,2,7]) # 4
find_greater_numbers([5,4,3,2,1]) # 0
find_greater_numbers([]) # 0
'''

def find_greater_numbers(lis):
    total = 0
    for i in range(len(lis)):
        for value in lis[i+1:]:
            if value > lis[i]:
                total += 1
    return total

print(find_greater_numbers([5,4,3,2,1]))
