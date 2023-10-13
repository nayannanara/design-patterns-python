from abc import ABC, abstractmethod

class ValidatorInterface():
    @abstractmethod
    def validate(self, comida: str) -> bool:
        pass

    @abstractmethod
    def action(self) -> bool:
        pass 