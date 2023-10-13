from strategy.skills.interfaces import SkillsInterface
from typing import Type

class Guerreiro:
    def __init__(self, skill: Type[SkillsInterface]) -> None:
        self.skill = skill

    def acao(self):
        self.skill.comportamento()

    def atributos(self):
        self.skill.nivel_atributo()        