from factory.interface.database import DatabaseInterface
from typing import Type

class Usecase:
    def __init__(self, repository: Type[DatabaseInterface]) -> None:
        self.__repository = repository

    def do_something(self) -> dict:
        return self.__repository.select_one()
    
