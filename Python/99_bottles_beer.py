def make_song(beverage, count=99):
    while True:
        if count == 1:
            yield 'Only ' + str(count) + ' bottle of ' + beverage + ' left!'
            count -= 1
        elif count == 0:
            yield "No more " + beverage + "!"
            raise StopIteration()
        else:
            yield str(count) + ' bottles of ' + beverage + ' on the wall.'
            count -= 1

k = make_song("beer")
for item in k:
    print(item)
