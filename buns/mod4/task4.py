word = input("Введите слово: ")

# создаем словарь, в котором будем хранить количество повторений каждой буквы
letters = {}

# перебираем каждую букву в слове
for letter in word:
    # если буква уже есть в словаре, увеличиваем ее количество повторений на 1
    if letter in letters:
        letters[letter] += 1
    # если буквы еще нет в словаре, добавляем ее со значением 1
    else:
        letters[letter] = 1

# определяем количество букв с нечетным количеством повторений
odd_count = 0
for count in letters.values():
    if count % 2 != 0:
        odd_count += 1

# если количество букв с нечетным количеством повторений не превышает 1, то можно составить палиндром
if odd_count <= 1:
    # создаем список из букв, которые будут находиться в середине палиндрома (если они есть)
    middle_letters = [letter*count for letter, count in letters.items() if count % 2 != 0]
    # создаем список из букв, которые будут находиться по краям палиндрома
    side_letters = [letter for letter, count in letters.items() if count % 2 == 0]
    # создаем список палиндрома, объединяя буквы по краям и в середине (если они есть)
    palindrome = side_letters + middle_letters + side_letters[::-1]
    # выводим палиндром на экран
    print("".join(palindrome))
else:
    print("Из данного слова нельзя составить палиндром.")