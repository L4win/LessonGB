count = int(input('Введите число:'))
max_num = count % 10
count = count // 10
while count > 0:
    if count % 10 > max_num:
        max_num = count % 10
    count = count // 10
print("Максимальное число:", max_num)
