string = input("Введите доменное имя сайта: ").split(".")
for part in reversed(string):
    print(part)