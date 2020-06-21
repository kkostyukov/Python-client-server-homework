# Есть файл orders в формате JSON с информацией о заказах. Написать скрипт,
# автоматизирующий его заполнение данными.
# Для этого:
# * Создать функцию write_order_to_json(), в которую передается 5
# параметров — товар (item), количество (quantity), цена (price),
# покупатель (buyer), дата (date). Функция должна предусматривать запись
# данных в виде словаря в файл orders.json. При записи данных указать
# величину отступа в 4 пробельных символа;
# * Проверить работу программы через вызов функции write_order_to_json()
# с передачей в нее значений каждого параметра.
import json


def write_order_to_json(item, quantity, price, buyer, date):
    with open('orders.json') as f_n:
        obj = json.load(f_n)

    order = {
        'товар': item,
        'количество': quantity,
        'цена': price,
        'покупатель': buyer,
        'дата': date,
    }

    obj['orders'].append(order)
    with open('orders.json', 'w') as f_n:
        json.dump(obj, f_n, indent=4)


write_order_to_json('стол', '1', '30000', 'Он', '01/02/2020')
