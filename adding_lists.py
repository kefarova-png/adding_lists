def input_list(list_number):
    while True:
        try:
            input_str = input(f"Введите числа {list_number}-го списка через пробел: ")
            list_str = input_str.split()
            list_i = [float(num) for num in list_str]
            if len(list_i) > 0:
                print(f"Ваш {list_number}-й список чисел:", list_i)
                return list_i
            print('Введённые данные не содержат чисел.')
        except ValueError:
            print('''Ошибка: невозможно создать список по введенным данным.
В следующий раз вводите, пожалуйста, только числа и пробелы.''')


def adding_list_elements(list_1, list_2):
    min_lenght = min(len(list_1), len(list_2))
    sum_list = []
    for n in range(0, min_lenght):
        sum_element = list_1[n] + list_2[n]
        sum_list.append(sum_element)
    if len(list_1) > len(list_2):
        for n in range(min_lenght, len(list_1)):
            sum_list.append(list_1[n])
    if len(list_2) > len(list_1):
        for n in range(min_lenght, len(list_2)):
            sum_list.append(list_2[n])
    return sum_list


list_1 = input_list(1)
list_2 = input_list(2)
sum_list = adding_list_elements(list_1, list_2)
print("Ваши суммы чисел", sum_list)