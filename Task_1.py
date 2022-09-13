# 1 - Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр. 
# Учтите, что числа могут быть отрицательными

# Пример:
# 67.82 -> 23
# 0.56 -> 11

number = input('Введи вещественное число: ')
number_list = number.split('.')
sum = 0
for item in number_list:
    item = abs(int(item))
    while item != 0:
        sum += item % 10
        item //= 10
print(sum)