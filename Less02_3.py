num = int(input("Enter month number:"))
if num <= 12 and num >= 1:
    month_dict = {1: 'January',
                  2: 'February',
                  3: 'March',
                  4: 'April',
                  5: 'May',
                  6: 'June',
                  7: 'Jule',
                  8: 'August',
                  9: 'September',
                  10: 'October',
                  11: 'November',
                  12: 'December'}
    month = list(month_dict.values())
    for i, el in enumerate(month):
        if i == num - 1:
            print(month[i])
