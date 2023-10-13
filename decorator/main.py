def decorator(item):
    def wrapper(*args, **kwargs):
        print('oi')
        item(*args, **kwargs)
    return wrapper


class Teste:
    @decorator
    def metodo(self):
        print('teste')

teste = Teste().metodo()