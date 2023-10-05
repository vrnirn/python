string = input("Введите строку: ")
zeros = units = 0
for i in string:
        if i == "0": zeros +=1
        else: units += 1
if zeros == units: print ('yes')
else: print('no')