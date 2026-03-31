def input_lenght_of_lists():
    text_of_error = '''Ошибка: невозможно создать списки заданной длины.
В следующий раз введите, пожалуйста, целое положительное число.'''
    while True:
        try:
            lenght = int(input('Введите длину генерируемых списков (целое положительное число): '))
            if lenght > 0:
                return lenght
            print(text_of_error)
        except ValueError:
            print(text_of_error)


def generator_of_lists(lenght):
    list_1 = [(x+1)*10 for x in range(0, lenght)]
    list_2 = [(x+1)*(-1) for x in range(0, lenght)]
    return list_1, list_2


def adding_list_elements(list_1, list_2, lenght):
    sum_list = []
    for n in range(0, lenght):
        sum_element = list_1[n] + list_2[n]
        sum_list.append(sum_element)
    return sum_list


lenght = input_lenght_of_lists()
list_1, list_2 = generator_of_lists(lenght)
sum_list = adding_list_elements(list_1, list_2, lenght)
print(sum_list)
