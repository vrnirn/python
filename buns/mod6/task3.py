def get_armstrong_numbers(number):
    for num in range(number):
        n = len(str(num))
        sum = 0
        for digit in str(num):
            sum += int(digit) ** n
        if sum == num:
            yield num

for num in get_armstrong_numbers(1000):
    print(num)
