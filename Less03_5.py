def sum_num():
    s = 0
    a = input("Enter the numbers separated by a space, input 'q' to exit: ")
    while a != "q":
        in_list = a.split()
        for num in in_list:
            try:
                s += int(num)
            except ValueError:
                print("To complete, type 'q'")
        print(f'Sum of numbers = {s}')
        a = input("Enter the numbers separated by a space, input 'q' to exit: ")
    else:
        return f'Sum of numbers = {s}'


print(sum_num())
