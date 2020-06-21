# . Задание на закрепление знаний по модулю CSV.
#
# Написать скрипт, осуществляющий выборку определенных данных из файлов info_1.txt,
# info_2.txt, info_3.txt и формирующий новый «отчетный» файл в формате CSV.
# Для этого:
# * Создать функцию get_data(), в которой в цикле осуществляется перебор файлов
# с данными, их открытие и считывание данных. В этой функции из считанных данных
# необходимо с помощью регулярных выражений извлечь значения параметров
# «Изготовитель системы»,«Название ОС», «Код продукта», «Тип системы». Значения
# каждого параметра поместить в соответствующий список. Должно получиться четыре
# списка — например, os_prod_list, os_name_list, os_code_list, os_type_list.
# В этой же функции создать главный список для хранения данных отчета — например,
# main_data — и поместить в него названия столбцов отчета в виде списка:
# «Изготовитель системы», «Название ОС», «Код продукта», «Тип системы».
# Значения для этих столбцов также оформить в виде списка и поместить в
# файл main_data (также для каждого файла);
# * Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл.
# В этой функции реализовать получение данных через вызов функции get_data(),
# а также сохранение подготовленных данных в соответствующий CSV-файл;
# * Проверить работу программы через вызов функции write_to_csv().

import csv
import re


def get_date(files):
    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []
    # main_data = [['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']]
    main_data = [os_prod_list, os_name_list, os_code_list, os_type_list]

    for file in files:
        with open(file) as f_n:
            f_n_reader = f_n.read()
            res = re.search(r'Изготовитель системы.*', f_n_reader)
            os_prod_list.append(re.sub(r'Изготовитель системы:\s*', '', res.group()))
            res = re.search(r'Название ОС.*', f_n_reader)
            os_name_list.append(re.sub(r'Название ОС:\s*', '', res.group()))
            res = re.search(r'Код продукта.*', f_n_reader)
            os_code_list.append(re.sub(r'Код продукта:\s*', '', res.group()))
            res = re.search(r'Тип системы.*', f_n_reader)
            os_type_list.append(re.sub(r'Тип системы:\s*', '', res.group()))

    main_data = list(map(list, zip(*main_data)))
    main_data.insert(0, ['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы'])
    return main_data


def write_to_csv(file):
    data_files = ['info_1.txt', 'info_2.txt', 'info_3.txt']
    main_data = get_date(data_files)
    with open(file, 'w') as f_n:
        f_n_writer = csv.writer(f_n)
        for row in main_data:
            f_n_writer.writerow(row)


write_to_csv('main_data.csv')
