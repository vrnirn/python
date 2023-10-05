side = float(input("Введите длину стороны квадрата: "))

p = round(side*4, 2)
s = round(side**2, 2)
d = round(side*2**(1/2), 2)

print(p, s, d)