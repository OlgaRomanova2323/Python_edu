# Дополнить справочник возможностью копирования данных из одного файла в другой.
# Пользователь вводит номер строки, которую необходимо перенести из одного файла в другой.
from csv import DictReader, DictWriter
from os.path import exists
class NameError(Exception):
    def __init__(self, txt):
        self.txt = txt


def get_data():
    flag = False
    while not flag:
        try:
            first_name = input("Введите имя: ")
            if len(first_name) < 2:
                raise NameError("Слишком короткое имя")
            last_name = input("Введите фамилию: ")
            if len(last_name) < 2:
                raise NameError("Слишком короткая фамилия")
            phone = input('Введите номер телефона: ')
            if len(phone) < 12:
                raise NameError("Слишком короткий номер")
        except NameError as err:
            print(err)
        else:
            flag = True
    return [first_name, last_name, phone]


def create_file(filename):
    with open(filename, 'w', newline='', encoding='utf-8') as data:
        f_w = DictWriter(data, fieldnames=['Имя', 'Фамилия', 'Телефон'])
        f_w.writeheader()


def read_file(filename):
    with open(filename, 'r', newline='', encoding='utf-8') as data:
        f_r = DictReader(data)
        return list(f_r)


def write_file(filename, lst):
    res = read_file(filename)
    obj = {'Имя': lst[0], 'Фамилия': lst[1], 'Телефон': lst[2]}
    res.append(obj)
    standard_write(filename, res)


def row_search(filename):
    last_name = input("Введите фамилию: ")
    res = read_file(filename)
    for row in res:
        if last_name == row['Фамилия']:
            return row
    return ("Запись не найдена")


def delete_row(filename):
    res = read_file(filename)
    row_number = int(input('Введите номер строки: '))
    res.pop(row_number-1)
    standard_write(filename, res)


def standard_write(filename, res):
    with open(filename, 'w', newline='', encoding='utf-8') as data:
        f_w = DictWriter(data, fieldnames=['Имя', 'Фамилия', 'Телефон'])
        f_w.writeheader()
        f_w.writerows(res)


def change_row(filename):
    res = read_file(filename)
    row_number = int(input('Введите номер строки: '))
    data = get_data()
    res[row_number - 1]["Имя"] = data[0]
    res[row_number - 1]["Фамилия"] = data[1]
    res[row_number - 1]["Телефон"] = data[2]
    standard_write(filename, res)

def copy_row_to_file(filename, filename1):
    res = read_file(filename)
    copy_res = list()
    row_number = int(input('Введите номер копируемой строки: '))
    copy_res.append(res[row_number - 1])
    standard_write(filename1, copy_res)





filename = 'phone.csv'
filename1 = 'copy_row.csv'


def main():
    while True:
        command = input("Введите команду: ")
        if command == "q":
            break
        elif command == 'w':
            if not exists(filename):
                create_file(filename)
            write_file(filename, get_data())
        elif command == 'r':
            if not exists(filename):
                print('Файл не существует. Создайте файл.')
                continue
            print(read_file(filename))
        elif command == 'f':
            if not exists(filename):
                print('Файл не существует. Создайте файл.')
                continue
            print(row_search(filename))
        elif command == 'd':
            if not exists(filename):
                print('Файл не существует. Создайте файл.')
                continue
            delete_row(filename)
        elif command == 'c':
            if not exists(filename):
                print('Файл не существует. Создайте файл.')
                continue
            change_row(filename)
        elif command == 'cr':
            create_file(filename1)
            copy_row_to_file(filename, filename1)


main()
