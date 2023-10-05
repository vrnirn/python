s = input("Введите строку: ")
a = ""
b = ""
comma = False

for i in s:
    if i == ",":
        comma = True
    elif not comma:
        a += i
    else:
        b += i

a = str(a)
b = str(b).replace(' ', '')

count = 0
for i in a:
    if i == b:
        count += 1
    else:
        break
print("Количество символов", a, "в начале строки:", count)

