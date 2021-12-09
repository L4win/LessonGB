def my_func(arg1, arg2, arg3):
    print(f'The sum of the largest two arguments is: {arg1 + arg2 + arg3 - min([arg1, arg2, arg3])}')


my_func(int(input('Enter Argument 1: ')), int(input('Enter Argument 2: ')), int(input('Enter Argument 3: ')))
