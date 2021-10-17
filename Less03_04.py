def my_func(x, y):
    return x ** y


def my_func_2(x, y):
    count = 1
    result = 1 / x
    while count < abs(y):
        result = result * (1 / x)
        count += 1
    return result


try:
    print(f'1 location: {my_func(float(input("Enter x:")), int(input("Enter y:")))}')
except ValueError as e:
    print(e)
except TypeError as f:
    print(f)

try:
    print(f'2 location: {my_func_2(float(input("Enter x: ")), int(input("Enter y: ")))}')
except ValueError as e:
    print(e)
except TypeError as f:
    print(f)

