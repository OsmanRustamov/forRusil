from typing import Union


# 102936456214652135727561205, 92057275512051510293645621465513572755120529364562146275512
# 72750120615, 77776710012
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
        user_first_num = input("Введите первое число: ")
        user_second_num = input("Введите второе число: ")
        result = str(int(user_first_num) + int(user_second_num))

        print(conversion_to_another_number_system(result, int))

    case "2":
        user_first_num = input("Введите первое число: ")
        user_second_num = input("Введите второе число: ")
        result = str(int(user_first_num) + int(user_second_num))

        print(conversion_to_another_number_system(result, oct))
    case "3":
        user_first_num = input("Введите первое число: ")
        user_second_num = input("Введите второе число: ")
        result = str(int(user_first_num) + int(user_second_num))

        print(conversion_to_another_number_system(result, bin))
    case "4":
        user_first_num = input("Введите первое число: ")
        user_second_num = input("Введите второе число: ")
        result = str(int(user_first_num) + int(user_second_num))

        print(conversion_to_another_number_system(result, hex))
    case _:
        print("Ошибка!\nВведите вариант от 1 до 4")
