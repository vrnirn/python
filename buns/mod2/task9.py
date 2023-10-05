string = input("Введите строку: ")
a_count = b_count = 0;
for i in string:
    if i == 'а' or i == 'е' or  i == 'ё' or i == 'и' or i == 'о' or i == 'у' or i == 'ы' or i == 'э' or i == 'ю' or i == 'я':
        a_count += 1
    elif i == ' ': continue
    else: b_count += 1
print(a_count, b_count)