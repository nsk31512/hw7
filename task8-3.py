'''
3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел. Проверить
работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список. Класс-исключение
 должен контролировать типы данных элементов списка.
Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу
скрипта, введя, например, команду “stop”. При этом скрипт завершается, сформированный список выводится на экран.
Подсказка: для данного задания примем, что пользователь может вводить только числа и строки. При вводе пользователем
очередного элемента необходимо реализовать проверку типа элемента и вносить его в список, только если введено число.
Класс-исключение должен не позволить пользователю ввести текст (не число) и отобразить соответствующее сообщение.
При этом работа скрипта не должна завершаться.
'''


class NumbersInList(Exception):

    @classmethod
    def checking(cls, arg):
        if arg.isalpha():
            return 'string'
        elif '.' not in arg:
            return 'int'
        elif '.' in arg:
            return 'float'


print('Вводите числа, пока не надоест :). Если надоело, введите stop.')
list_of_numbers = []
while True:
    argument = input()
    if argument == 'stop':
        break
    elif NumbersInList.checking(argument) == 'int':
        list_of_numbers.append(int(argument))
    elif NumbersInList.checking(argument) == 'float':
        list_of_numbers.append(float(argument))
    elif NumbersInList.checking(argument) == 'string':
        print('Вы ввели строку, а не число. Введите число: ', end='')

print(list_of_numbers)
