words = input('Введите список слов через пробел: ').split()
result = ''.join([word[-1] for word in words])
print(result)