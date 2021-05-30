'''
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту
ситуацию и не завершиться с ошибкой.
'''


class MyZeroDivision(Exception):

    def __init__(self, num):
        self.num = num

    def __str__(self):
        if self.num == 0:
            return 'MyZeroDivision: Попытка деления на ноль!'


num1 = int(input('Введите первое число: '))
num2 = int(input('Введите второе число: '))
try:
    if num2 == 0:
        raise MyZeroDivision(num2)
    else:
        result = num1 / num2
    print(f'Число 1 разделить на число 2 равно {result}')
except MyZeroDivision as my_err:
    print(my_err)
