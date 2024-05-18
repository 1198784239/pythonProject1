def my_gen():
    n = 1
    print('this is first')
    yield n

    n += 1
    print('this is second')
    yield n

    n += 1
    print('this is last')
    yield n


for i in my_gen():
    print(i)