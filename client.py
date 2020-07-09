import json
import socket
import time
import logging
import log.client_log_config
from decorators import log

from utils import get_message, send_message, get_pars
from project_settings import ACTION, PRESENCE, USER, TIME, ACCOUNT_NAME, RESPONSE, ERROR, SERVER_ANSWERS, FROM,\
    ENCODING, MESSAGE, TO, MSG

LOGGER = logging.getLogger('client')


@log
def create_presence(account_name='Guest'):
    """Функция генерирует запрос о присутствии клиента."""
    out = {
        ACTION: PRESENCE,
        TIME: time.time(),
        USER: {
            ACCOUNT_NAME: account_name
        }
    }
    LOGGER.debug(f'Сформировано {PRESENCE} сообщение для пользователя {account_name}')
    return out


def create_msg(msg: str, account_name='Guest', receiver='server'):
    out = {
        ACTION: MSG,
        TIME: time.time(),
        TO: receiver,
        FROM: account_name,
        'encoding': ENCODING,
        MESSAGE: msg
    }
    return out


def process_ans(message):
    """Функция разбирает ответ сервера."""
    if RESPONSE in message:
        if message[RESPONSE] in SERVER_ANSWERS:
            return f'{message[RESPONSE]}: {SERVER_ANSWERS[message[RESPONSE]]}'
        else:
            return message[RESPONSE]
    else:
        return f'400 : {message[ERROR]}'


def main():
    # Инициализация сокета и обмен.
    transport = socket.socket()
    transport.connect(get_pars())
    message_to_server = create_presence()
    send_message(transport, message_to_server)
    try:
        answer = process_ans(get_message(transport))
        LOGGER.info(f'Принят ответ от сервера {answer}')
        print(answer)
    except (ValueError, json.JSONDecodeError):
        print('Не удалось декодировать сообщение сервера.')
    transport = socket.socket()
    transport.connect(get_pars())
    message_to_server = create_msg('Привет')
    send_message(transport, message_to_server)
    try:
        answer = process_ans(get_message(transport))
        LOGGER.info(f'Принят ответ от сервера {answer}')
        print(answer)
    except (ValueError, json.JSONDecodeError):
        LOGGER.error('Не удалось декодировать полученную Json строку.')
        print('Не удалось декодировать сообщение сервера.')


if __name__ == '__main__':
    main()
