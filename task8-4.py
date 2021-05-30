'''
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
уникальные для каждого типа оргтехники.
'''


class Storage:

    def __init__(self, name):
        self.name = name


class OfficeEquipment:
    def __init__(self, name, brand, model):
        self.model = model
        self.brand = brand
        self.name = name


class Printer(OfficeEquipment):
    @classmethod
    def printing(cls, txt: object) -> object:
        return txt


class Scanner(OfficeEquipment):
    @classmethod
    def scanning(cls):
        txt = input('Что нужно остканировать?')
        return txt


class Copier (Scanner, Printer):
    @classmethod
    def scanning(cls):
        txt = input('Что нужно откопировать?')
        return txt


my_storage = Storage('Склад компьютерной техники')
printer1 = Printer('printer', 'HP', 'M1001')
print_file = printer1.printing('Пробная страница')
print(f'{printer1.brand, printer1.model} Напечатал лист с текстом: {print_file}')
print('-' * 10)

scanner1 = Scanner('scanner', 'Kyocera', 'F1000')
scan_file = scanner1.scanning()
print(f'{scanner1.brand, scanner1.model} отсканировал: {scan_file}')
print('-' * 10)

copier1 = Copier('copier', 'HP', 'Mastercopy 2000')
copied_file = copier1.scanning()
print(f'{copier1.brand, copier1.model} отсканировал и вывел на печать: {copied_file}')
print('-' * 10)
