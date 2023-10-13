from chain_of_responsability.validators.banana import BananaValidator
from chain_of_responsability.validators.carne import CarneValidator


class Validation:
    def __init__(self) -> None:
        self.validators = [
            BananaValidator(),
            CarneValidator()
        ]    
    
    def process(self, comida: str):
        for v in self.validators:
            if v.validate(comida): return v.action()


validation = Validation()
validation.process('banana')