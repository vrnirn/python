number = int(input())
number_b = number_o = number_h = number

binary = octal = hexadecimal = ""

if number <=0:
    print('Неверный ввод!')
while number_b>0:
    binary += str(number_b%2)
    number_b //= 2
    
while number_o>0:
    octal += str(number_o%8)
    number_o //= 8

while number_h>0:
    remainder = number_h%16
    if remainder < 10:
        hexadecimal += str(number_h%16)
    else:
        hexadecimal += chr(remainder + 87)
    number_h //= 16
    
print(binary[::-1], octal[::-1], hexadecimal[::-1])