# <p>Write a function called sum_up_diagonals which accepts an
# NxN list of lists and sums the two main diagonals in the array: the one from
# the upper left to the lower right, and the one from the upper right to the
# lower left.</p>

def sum_up_diagonals(matrix):
    dec = len(matrix) - 1
    total = 0
    for item in range(len(matrix)):
        total += matrix[item][item] + matrix[item][dec]
        dec -= 1
    return total

print(sum_up_diagonals(list2))
