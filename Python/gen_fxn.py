def count_up_to(x):
    count = 1
    while count <= x:
        yield count
        count +=1

k = count_up_to(10)
k = list(k)
for item in k:
    print(item)
