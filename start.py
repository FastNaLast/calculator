def calculate():
    try:
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))
    except ValueError:
        print("Ошибка: нужно вводить только числа.")
        return
    operation = input("Выберите операцию (+, -, *, /): ")
    if operation not in ['+', '-', '*', '/']:
        print("Ошибка: можно вводить только знаки +, -, *, / (слова и буквы нельзя!)")
        return 
    if operation == '+':
        print(f"Результат: {num1} + {num2} = {num1 + num2}")
    elif operation == '-':
        print(f"Результат: {num1} - {num2} = {num1 - num2}")
    elif operation == '*':
        print(f"Результат: {num1} * {num2} = {num1 * num2}")
    elif operation == '/':
        if num2 == 0:
            print("Ошибка: деление на ноль невозможно")
        else:
            print(f"Результат: {num1} / {num2} = {num1 / num2}")
    else:
        print("Неизвестная операция.")

calculate()