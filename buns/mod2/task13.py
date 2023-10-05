barcode = input("Введите штрих-код: ")
odd_sum = 0
even_sum = 0
for i in range(len(barcode)):
    if i % 2 == 0:
        odd_sum += int(barcode[i])
    else:
        even_sum += int(barcode[i])

if (even_sum * 3 + odd_sum) % 10 == 0:
    print('yes')
else:
    print('no')