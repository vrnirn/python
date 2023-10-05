s = input("Введите доменное имя сайта: ")
temp = ""
result = ""
for i in range(len(s)):
    if s[i] == ".":
        result = temp + "\n" + result
        temp = ""
    else:
        temp += s[i]
result = temp + "\n" + result
print(result)

