ratings = [7, 5, 3, 3, 2]
rating = float(input("Enter num rating:"))
i = 0
for n in ratings:
    if rating <= n:
        i += 1
    else:
        break
ratings.insert(i, rating)
print(ratings)