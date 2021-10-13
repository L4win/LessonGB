print("I can turn over the values that are worth it! Let's get started!")
print("To do this, you will have to enter a couple")
my_list = []
answer = ""
while answer != "q":
    answer = input("Are we going to enter numbers? (Y/N/Q)")
    if answer == 'Y':
        f = input("Enter num:")
        my_list.append(f)
    if answer == 'N':
        print("Goodbye", my_list, "This is what you entered")
        break
    if answer == 'q':
        print("Thanks for stopping by")
        break
if len(my_list) % 2 == 0:
    i = 0
    while i < len(my_list):
        el = my_list[i]
        my_list[i] = my_list[i + 1]
        my_list[i + 1] = el
        i += 2
else:
    i = 0
    while i < len(my_list) - 1:
        el = my_list[i]
        my_list[i] = my_list[i + 1]
        my_list[i + 1] = el
        i += 2
    print(my_list, "I've turned the numbers over for you here")
