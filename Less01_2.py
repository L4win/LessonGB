sec = int(input("Введите число:"))

hour = sec // 3600
sec %= 3600
minute = sec // 60
sec %= 60
print("Ваше число в формате времени:")
if hour < 10 and minute < 10 and sec < 10:
    print(f"0{hour}:0{minute}:0{sec}")
else:
    print(f"{hour}:{minute}:{sec}")
