'''
5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в
определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также других
 данных, можно использовать любую подходящую структуру, например словарь.
'''


class Storage:
    __products_list = []
    __transferred_products = []

    def __init__(self, name):
        self.name = name

    def append_to_storage(self, arg):
        """Функция приема техники на склад"""
        if len(Storage.__products_list) > 0:
            key_in_arg = str()
            for key in arg.keys():
                key_in_arg = key
                break
            for i in range(len(Storage.__products_list)):
                if Storage.__products_list[i].keys() == arg.keys():
                    new_value = Storage.__products_list[i][key_in_arg] + arg[key_in_arg]
                    Storage.__products_list[i][key_in_arg] = new_value
                    break
                elif Storage.__products_list[i].keys() != arg.keys() and i == len(Storage.__products_list) - 1:
                    Storage.__products_list.append(arg)
        else:
            Storage.__products_list.append(arg)

    def take_from_storage(self, arg):
        """Функция передачи техники в магазин"""
        key_in_arg = str()
        for key in arg.keys():
            key_in_arg = key
            break
        if arg.keys() not in Storage.__transferred_products:
            for i in range(len(Storage.__products_list)):
                if Storage.__products_list[i].keys() == arg.keys():
                    new_value = Storage.__products_list[i][key_in_arg] - arg[key_in_arg]
                    Storage.__products_list[i][key_in_arg] = new_value
                    Storage.__transferred_products.append(arg)
                    break
        else:
            for i in range(len(Storage.__products_list)):
                if Storage.__products_list[i].keys() == arg.keys():
                    new_value = Storage.__products_list[i][key_in_arg] - arg[key_in_arg]
                    Storage.__products_list[i][key_in_arg] = new_value
                    Storage.__transferred_products[i][key_in_arg] = arg[key_in_arg]
                    break

    def __str__(self):
        """Выводит информацию о товарах, хранящихся на складе"""
        print('На складе хранятся следующие товары:')
        line_str = str()
        for item in Storage.__products_list:
            line_str += str(item) + '\n'
        return line_str

    @staticmethod
    def transferred_products_information():
        """Выводит информацию о товарах, переданых в магазин"""
        print('В магазин переданы:')
        for item in Storage.__transferred_products:
            print(item)


class OfficeEquipment:
    def __init__(self, name, brand, model):
        self.model = model
        self.brand = brand
        self.name = name

    def format_to_storage(self, number):
        """Функция для передачи информации о товаре на склад
        number - количиство товара"""
        return {f'{self.name, self.brand, self.model}': number}


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
my_storage.append_to_storage(printer1.format_to_storage(5))

scanner1 = Scanner('scanner', 'Kyocera', 'F1000')
my_storage.append_to_storage(scanner1.format_to_storage(10))

copier1 = Copier('copier', 'HP', 'Mastercopy2000')
my_storage.append_to_storage(copier1.format_to_storage(20))

print(my_storage)

my_storage.append_to_storage(printer1.format_to_storage(23))
print(my_storage)

try:
    my_storage.take_from_storage(printer1.format_to_storage(3))
    my_storage.take_from_storage(copier1.format_to_storage(7))
    my_storage.take_from_storage(scanner1.format_to_storage(1))
except NameError:
    print('Данный товар отсутствует на складе')

print(my_storage)

Storage.transferred_products_information()
