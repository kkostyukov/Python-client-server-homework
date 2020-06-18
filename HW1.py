import subprocess

import chardet

# 1. Каждое из слов «разработка», «сокет», «декоратор» представить
# в строковом формате и проверить тип и содержание соответствующих
# переменных. Затем с помощью онлайн-конвертера преобразовать
# строковые представление в формат Unicode и также проверить тип и
# содержимое переменных.
print('Задание 1:')
words = ['разработка', 'сокет', 'декоратор']
for element in words:
    print(f'Значение - {element}, тип - {type(element)}')
bytes_words = ['\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430',
               '\u0441\u043e\u043a\u0435\u0442',
               '\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440']
for element in bytes_words:
    print(f'Значение - {element}, тип - {type(element)}')

# 2. Каждое из слов «class», «function», «method» записать в байтовом
# типе без преобразования в последовательность кодов (не используя
# методы encode и decode) и определить тип, содержимое и длину
# соответствующих переменных.
print('Задание 2:')
words = [b'class', b'function', b'method']
for element in words:
    print(f'Значение {element}, тип {type(element)}, длина {len(element)}')

# 3. Определить, какие из слов «attribute», «класс», «функция»,
# «type» невозможно записать в байтовом типе.
print('Задание 3:')
words = ['attribute', 'класс', 'функция', 'type']
for element in words:
    try:
        bytes(element, 'ascii')
        print(f'Слово "{element}" можно записать в байтовом типе')
    except UnicodeEncodeError:
        print(f'Слово "{element}" нельзя записать в байтовом типе')


# 4. Преобразовать слова «разработка», «администрирование»,
# «protocol», «standard» из строкового представления в
# байтовое и выполнить обратное преобразование (используя методы
# encode и decode).
print('Задание 4:')
words = ['разработка', 'администрирование', 'protocol', 'standard']
for num_element in range(len(words)):
    words[num_element] = words[num_element].encode('utf-8')
print(words)
for num_element in range(len(words)):
    words[num_element] = words[num_element].decode('utf-8')
print(words)

# 5. Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
#  преобразовать результаты из байтовового в строковый тип на
# кириллице.
print('Задание 5:')


def result_out(subproc_ping: subprocess):
    for line in subproc_ping.stdout:
        result = chardet.detect(line)
        line = line.decode(result['encoding']).encode('utf-8')
        print(line.decode('utf-8'))


result_out(subprocess.Popen(['ping', 'yandex.ru'], stdout=subprocess.PIPE))
result_out(subprocess.Popen(['ping', 'youtube.ru'], stdout=subprocess.PIPE))

# 6. Создать текстовый файл test_file.txt, заполнить его тремя
# строками: «сетевое программирование», «сокет», «декоратор».
# Проверить кодировку файла по умолчанию. Принудительно открыть
# файл в формате Unicode и вывести его содержимое.
print('Задание 6:')
new_file = open('test_file.txt', 'w', encoding='utf-8')
new_file.write('сетевое программирование\nсокет\nдекоратор')
new_file.close()


with open('test_file.txt', encoding='utf-8') as f_n:
    for el_str in f_n:
        print(el_str, end='')
