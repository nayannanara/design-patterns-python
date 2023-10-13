from core.controller import insert_data
from core.adapter import Adapter


def router1(message):
    process = Adapter(Code())
    process.handle(message)


class Code:
    def handle(self, message):
        token = message['header']['token']
    
        if token:
            print('Autenticando o token')
            insert_data(message['body']['name'], message['body']['message'])