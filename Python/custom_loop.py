#defining our own for loop using recursion
# def loop(iterator):
#     try:
#         if type(iterator) == type(iter([1,2])):
#             print(next(iterator))
#             loop(iterator)
#         else:
#             i = iter(iterator)
#             print(next(i))
#             loop(i)
#
#     except StopIteration:
#         return 1

#using forever loop + break
def loop(it, fn):
    itrtr = iter(it)
    while True:
        try:
            fn(next(itrtr))
        except StopIteration:
            # print("End of Iterator")
            break
    return 1

def square(x):
    print(x*x)

x = [1,2,3,4,5]
loop(x, print)
loop(x, square)
