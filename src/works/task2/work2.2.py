# 102936456214652135727561205, 92057275512051510293645621465513572755120529364562146275512
# 72750120615, 77776710012
def conversion_to_another_number_system(num_str1: str, num_str2: str, number_system_type):
    numbers_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    num_str_list = [num_str1, num_str2]
    result = 0

    for num_str in num_str_list:
        if number_system_type == "1":
            if not num_str.isdigit():
                return "Ошибка!\nИмеется буква"
            result += int(num_str)

        elif number_system_type == "2":
            for number in num_str:
                if number not in numbers_list[:8]:
                    return "Несоответствие числа заданной системе счисления"
            result += int(num_str, 8)

        elif number_system_type == "3":
            for number in num_str:
                if number not in ['0', '1']:
                    return "Несоответствие числа заданной системе счисления"
            result += int(num_str, 2)

        elif number_system_type == "4":
            for number in num_str:
                if number not in numbers_list:
                    return "Ошибка!\nИмеется буква"
            result += int(num_str, 16)

    if number_system_type == "1":
        return result
    elif number_system_type == "2":
        return oct(result)[2:]
    elif number_system_type == "3":
        return bin(result)[2:]
    elif number_system_type == "4":
        return hex(result)[2:].upper()


if __name__ == '__main__':
    user_choice = input(
        "Выберите систему счисления:\n1) Десятичная (10-ичная)\n2) Восьмиричная (8-ичная)\n3) Двоичная (2-ичная)\n4) Шестнадцатиричная (16-ичная)\nВведите номер выбранной опции: ")

    if user_choice not in ["1", "2", "3", "4"]:
        print("Ошибка!\nВведите вариант от 1 до 4")
    else:
        user_first_num = input("Введите первое число: ").strip()
        user_second_num = input("Введите второе число: ").strip()

        print(conversion_to_another_number_system(user_first_num, user_second_num, user_choice))
