def div(s_1, s_2):
    try:
        s_1, s_2 = int(s_1), int(s_2)
        div_num = s_1 / s_2
    except ValueError:
        return  "You need to enter numbers"
    except ZeroDivisionError:
        return "You can't divide by zero"
    return round(div_num, 2)


print(div(input("Enter your first num: "), input("Enter your second num: ")))
