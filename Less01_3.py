n = int(input("Введите число n: "))
temp_value = str(n)
temp_one = temp_value + temp_value
temp_two = temp_value + temp_value + temp_value
amount = n + int(temp_one) + int(temp_two)
print("Результат равен:", amount, )
