from typing import Union


# 102936456214652135727561205, 92057275512051510293645621465513572755120529364562146275512
# 72750120615, 77776710012
def compare_numbers(num1: str, num2: str) -> str:
    if not num1.isdigit() or not num2.isdigit():
        return "Ошибка!\nИмеется буква"

    if int(num1) > int(num2):
        return "Первое число больше второго"
    elif int(num1) < int(num2):
        return "Первое число меньше второго"
    else:
        return "Числа равны"



x1 = input(
    "Выберите систему счисления:\n1) Десятичная (10-ичная)\n2) Восьмиричная (8-ичная)\n3) Двоичная (2-ичная)\n4) Шестнадцатиричная (16-ичная)\nВведите номер выбранной опции: ")

match x1:
    case "1":
        var1 = input("Введите первое число: ")
        var2 = input("Введите второе число: ")

        print(compare_numbers(var1, var2))

    case "2":
        var1 = input("Введите первое число: ")
        var2 = input("Введите второе число: ")

        print(compare_numbers(var1, var2))
    case "3":
        var1 = input("Введите первое число: ")
        var2 = input("Введите второе число: ")

        print(compare_numbers(var1, var2))
    case "4":
        var1 = input("Введите первое число: ")
        var2 = input("Введите второе число: ")

        print(compare_numbers(var1, var2))
    case _:
        print("Ошибка!\nВведите вариант от 1 до 4")
