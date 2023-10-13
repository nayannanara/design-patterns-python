from strategy.skills.interfaces import SkillsInterface


class UsoArco(SkillsInterface):
    def __init__(self, nivel) -> None:
        self.nivel = nivel
    
    def comportamento(self):
        print('atirar flechas')

    def nivel_atributo(self):
        print(f'nivel de uso arco: {self.nivel}')