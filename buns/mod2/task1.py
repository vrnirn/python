numbers = input("Введите два числа: ")
a = ""
b = ""
comma = False

for i in numbers:
    if i == ",":
        comma = True
    elif not comma:
        a += i
    else:
        b += i

a = int(a)
b = int(b)

print(a % b)