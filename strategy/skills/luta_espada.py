from strategy.skills.interfaces import SkillsInterface


class LutaEspada(SkillsInterface):
    def __init__(self, nivel) -> None:
        self.nivel = nivel
    
    def comportamento(self):
        print('lutar com espada')

    def nivel_atributo(self):
        print(f'nivel de uso espada: {self.nivel}')