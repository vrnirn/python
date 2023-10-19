filename = input("Введите имя файла: ")

with open(filename, 'r', encoding="utf-8") as file:
    data = file.read()

letters = {}
for letter in data:
    if letter.isalpha():
        letter = letter
        if letter in letters:
            letters[letter] += 1
        else:
            letters[letter] = 1

sorted_letters = sorted(letters.items(), key=lambda x: x[1])

with open('result.txt', 'w', encoding="utf-8") as file:
    for letter, count in sorted_letters:
        file.write(f"{letter}: {count}\n")