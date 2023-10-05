numberPhone = input('Введите номер телефона: ')

numberPhone = numberPhone.replace('-', '')\
.replace('(', '')\
.replace(')', '')\
.replace(' ', '')

print(numberPhone)