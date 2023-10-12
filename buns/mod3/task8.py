phone_number = input("Введите номер телефона: ")
phone_number = phone_number.replace("-", "").replace(")", "").replace("(", "").replace(" ", "")
print(phone_number)