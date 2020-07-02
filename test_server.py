import unittest
import time
from server import process_client_message

from project_settings import ACTION, PRESENCE, TIME, USER, ACCOUNT_NAME, RESPONSE, ERROR, FROM, MESSAGE, MSG, TO


class TestServer(unittest.TestCase):
    def setUp(self) -> None:
        self.resp_200 = {RESPONSE: 200}
        self.msg_ok = {RESPONSE: f'SERVER: Привет, Guest'}
        self.resp_err = {
            RESPONSE: 400,
            ERROR: 'неправильный запрос/JSON-объект'
        }

    def test_ok_presence(self):
        self.assertEqual(process_client_message(
            {ACTION: PRESENCE, TIME: time.time, USER: {ACCOUNT_NAME: 'Guest'}}), self.resp_200
        )

    def test_ok_msg(self):
        self.assertEqual(process_client_message({ACTION: MSG,
                                                 TIME: time.time,
                                                 FROM: 'Guest',
                                                 TO: 'server',
                                                 MESSAGE: 'Привет'}
                                                ), self.msg_ok
                         )
    def test_bad_request(self):
        self.assertEqual(process_client_message({ACTION: 'bad', TIME: time.time, USER: {ACCOUNT_NAME: 'Guest'}}
                                                ), self.resp_err
                         )
