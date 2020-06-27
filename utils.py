import json
import argparse
import sys
from project_settings import DEFAULT_IP_ADDRESS, ENCODING, MAX_PACKAGE_LENGTH, DEFAULT_PORT


def get_pars():
    """
    Утилита приема и возврата параметров из командной строки
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--adr', default=DEFAULT_IP_ADDRESS, help='Адрес сервера')
    parser.add_argument('-p', '--port', default=DEFAULT_PORT, help='Порт сервера', type=int)
    if parser.parse_args().port < 1024 or parser.parse_args().port > 65535:
        print('В качастве порта может быть указано только число в диапазоне от 1024 до 65535.')
        sys.exit(1)
    return parser.parse_args().adr, parser.parse_args().port

def get_message(client):
    """
    Утилита приёма и декодирования сообщения.

    Принимает байты выдаёт словарь, если принято что-то другое отдаёт ошибку значения.
    """
    encoded_response = client.recv(MAX_PACKAGE_LENGTH)
    if isinstance(encoded_response, bytes):
        json_response = encoded_response.decode(ENCODING)
        response = json.loads(json_response)
        if isinstance(response, dict):
            return response
        raise ValueError
    raise ValueError


def send_message(sock, message):
    """
    Утилита кодирования и отправки сообщения.

    Принимает словарь и отправляет его.
    """
    js_message = json.dumps(message)
    encoded_message = js_message.encode(ENCODING)
    sock.send(encoded_message)
