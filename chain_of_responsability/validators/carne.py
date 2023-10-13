from chain_of_responsability.validators.interface.validator import ValidatorInterface


class CarneValidator(ValidatorInterface):
    def validate(self, comida: str) -> bool:
        if comida == 'carne': return True
        return False
    
    def action(self) -> None:
        print('o leão come a carne')