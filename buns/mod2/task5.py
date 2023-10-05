i = input("Введите букву латинского алфавита: ")
n = int(input("Введите целое число: "))

if len(i) == 1 and i.isalpha() and i.islower() and isinstance(n, int):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    index_i = alphabet.index(i)
    index_k = (index_i + n) % len(alphabet)
    k = alphabet[index_k]
    print("Символ", i, "смещен на", n, "символов и равен", k)
else:
    print("Неверный ввод")