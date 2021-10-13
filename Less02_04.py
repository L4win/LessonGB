answer = input("Enter:").split()

for i, n in enumerate(answer, 1):
    if len(n) > 10:
        n = n[0:10]
    print(i, n)
