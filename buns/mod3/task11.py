field = []
k = int(input("Введите размер поля: "))

for i in range(k):
    row = input("Введите строку с символами для заполнения поля: ")
    field.append(list(row))

def check_winner(symbol):
    # Проверка строк
    for i in range(k):
        if field[i].count(symbol) == k:
            return True

    # Проверка столбцов
    for j in range(k):
        column = [field[i][j] for i in range(k)]
        if column.count(symbol) == k:
            return True

    # Проверка диагоналей
    diagonal1 = [field[i][i] for i in range(k)]
    diagonal2 = [field[i][k-1-i] for i in range(k)]
    if diagonal1.count(symbol) == k or diagonal2.count(symbol) == k:
        return True

    return False

if check_winner("X"):
    print("Победитель: X")
elif check_winner("O"):
    print("Победитель: O")
else:
    print("Ничья")