from typing import Union


def conversion_to_another_number_system(var: str, t: Union[int, oct, bin, hex]):
    if var.isdigit():
        if t != Union[int]:
            return t(int(var))[2:]
        return int(var)
    return "Ошибка!\nИмеется буква"


user_choice = input(
    "Выберите систему счисления:\n1) Десятичная (10-ичная)\n2) Восьмиричная (8-ичная)\n3) Двоичная (2-ичная)\n4) Шестнадцатиричная (16-ичная)\nВведите номер выбранной опции: ")

match user_choice:
    case "1":
        user_input = input("Введите число: ")

        print(conversion_to_another_number_system(user_input, int))
    case "2":
        user_input = input("Введите число: ")

        print(conversion_to_another_number_system(user_input, oct))
    case "3":
        user_input = input("Введите число: ")

        print(conversion_to_another_number_system(user_input, bin))
    case "4":
        user_input = input("Введите число: ")

        print(conversion_to_another_number_system(user_input, hex))
    case _:
        print("Ошибка!\nВведите вариант от 1 до 4")
