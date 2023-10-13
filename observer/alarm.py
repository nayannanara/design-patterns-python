from observer.interface.observer import Observer
from typing import Type


class Alarm:
    def __init__(self) -> None:
        self.beep = False
        self.people = []

    def add_person(self, person: Type[Observer]):
        self.people.append(person)

    def status(self):
        return self.beep
    
    def ring(self):
        self.beep = True

        for person in self.people:
            person.update()
        
        self.people = []


