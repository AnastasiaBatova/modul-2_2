my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
count = 0   # задаём счетчик
print(my_list)

while count < len(my_list):
    number = my_list[count]    # задаём число из списка
    count = count + 1   # запускаем счетчик
    if number == 0:
        continue
    elif number < 0:
        break
    elif count == len(my_list):
        print(number)
        print('Список закончился')
    else:
        print(number)