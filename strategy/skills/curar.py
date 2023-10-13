from strategy.skills.interfaces import SkillsInterface


class Curar(SkillsInterface):
    def __init__(self, nivel) -> None:
        self.nivel = nivel
    
    def comportamento(self):
        print('Curar personagem')

    def nivel_atributo(self):
        print(f'nivel de curao: {self.nivel}')