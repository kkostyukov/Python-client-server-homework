import unittest
import time

from client import process_ans, create_presence, create_msg
from project_settings import RESPONSE, ACTION, PRESENCE, TIME, USER, ACCOUNT_NAME, MSG, TO, FROM, ENCODING, \
    MESSAGE


class TestClient(unittest.TestCase):
    def test_create_presence(self):
        """Тест создания запроса приветствия серверу"""
        self.assertEqual(create_presence(), {ACTION: PRESENCE, TIME: time.time(), USER: {ACCOUNT_NAME: 'Guest'}})

    def test_create_msg(self):
        """Тест создания запроса сообщения серверу"""
        self.assertEqual(create_msg('Привет'), {ACTION: MSG, TIME: time.time(), TO: 'server', FROM: 'Guest',
                                                'encoding': ENCODING, MESSAGE: 'Привет'})

    def test_process_ans(self):
        """Тест создания разбора сообщений от сервера"""
        self.assertEqual(process_ans({RESPONSE: 200}), '200: OK')
        self.assertEqual(process_ans({RESPONSE: 400}), '400: неправильный запрос/JSON-объект')


class TestUtils(unittest.TestCase):
    pass
