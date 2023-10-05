numbers = input('Введите числа: ')
duplicates = False
for i in range(len(numbers)):
    for j in range(len(numbers)):
        if i != j:
            if numbers[i] == numbers[j] and numbers[i] != ' ':
                duplicates = True
                break
            
    break
print(duplicates)