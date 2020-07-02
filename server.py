import json
import socket
from utils import get_pars, get_message, send_message
from project_settings import ACTION, PRESENCE, USER, TIME, ACCOUNT_NAME, RESPONSE, RESPONSE_DEFAULT_IP_ADDRESS, ERROR, \
     MAX_CONNECTIONS, SERVER_ANSWERS, MSG, FROM, MESSAGE, TO


def process_client_message(message):
    """
    Обработчик сообщений от клиентов, принимает словарь - сообщение от клинта, проверяет корректность, возвращает
    словарь-ответ для клиента.
    """

    if (
            ACTION in message and
            message[ACTION] == PRESENCE and
            TIME in message and
            USER in message and
            message[USER][ACCOUNT_NAME] == 'Guest'
    ):
        return {
            RESPONSE: 200
        }
    elif (
            ACTION in message and
            message[ACTION] == MSG and
            TIME in message and
            MESSAGE in message and
            TO in message and
            FROM in message and
            message[FROM] == 'Guest'
    ):
        return {
            RESPONSE: f'SERVER: Привет, {message[FROM]}'
        }

    return {
        RESPONSE: 400,
        ERROR: SERVER_ANSWERS[400]
    }


def main():
    """
    Загрузка параметров командной строки, если нет параметров, то задаём значения по умоланию.

    server.py -a 127.0.0.1 -p 8888
    """
    # Готовим сокет
    transport = socket.socket()
    transport.bind(get_pars())
    # Слушаем порт
    transport.listen(MAX_CONNECTIONS)

    while True:
        client, client_address = transport.accept()
        try:
            message_from_client = get_message(client)
            print(message_from_client)
            response = process_client_message(message_from_client)
            send_message(client, response)
            client.close()
        except (ValueError, json.JSONDecodeError):
            print('Принято некорретное сообщение от клиента.')
            client.close()


if __name__ == '__main__':
    main()
