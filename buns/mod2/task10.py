string = input('Введите слова: ')
new_word = ""
word = ""
for char in string:
    if char != " ":
        word += char
    else:
        if word:
            new_word += word[-1]
        word = ""

if word:
    new_word += word[-1]

print(new_word)