def int_func(text):
    return text.title()


words = []
for word in input('Enter the word with a small letter: ').split():
    words.append(int_func(word))

print(f'It turns out the word: {" ".join(words)}')
