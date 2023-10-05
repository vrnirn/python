numbers = input("Введите три числа через пробел: ")
a = ""
b = ""
c = ""

i = 0
for char in numbers:
    if char != " ":
        if i == 0:
            a += char
        elif i == 1:
            b += char
        else:
            c += char
    else:
        i += 1
    
a = int(a)
b = int(b)
c = int(c)

if a < -1000 or a > 1000 or b < -1000 or b > 1000 or c < -1000 or c > 1000:
    print("Ошибка: все числа должны быть в диапазоне от -1000 до 1000")

else:
    if a > b:
        a, b = b, a
    if b > c:
        b, c = c, b
    if a > b:
        a, b = b, a

    print("Число, стоящее между двумя другими:", b)