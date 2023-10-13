from abc import ABC, abstractmethod


class SkillsInterface(ABC):
    @classmethod
    @abstractmethod
    def comportamento(self):
        pass

    @classmethod
    @abstractmethod
    def nivel_atributo(self):
        pass