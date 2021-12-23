my_file = open('01.txt', 'w', encoding='utf-8')
line = input('Введите текст \n')
while True:
    my_file.writelines(line)
    line = input('Введите текст \n')
    if not line:
        break

my_file.close()
my_file = open('01.txt', 'r')
content = my_file.readlines()
print(content)
my_file.close()
