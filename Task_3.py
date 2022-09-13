number = input('Введи большое число: ')

if number.isdigit():
    n_list = list(number)
    n_list.reverse()
    number_second = "".join(n_list)
        
    if number == number_second:
        print(f"Число {number} является палиндромом.")
    else:
        print(f"Число {number} НЕ является палиндромом.")

else:
    print("Это не число, попробуй ещё")