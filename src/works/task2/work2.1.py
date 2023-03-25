from typing import Union


def conversion_to_another_number_system(num_str: str, number_system_type: Union[int, oct, bin, hex]):
    if num_str.isdigit():
        if number_system_type != Union[int]:
            return number_system_type(int(num_str))[2:]
        return int(num_str)
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
