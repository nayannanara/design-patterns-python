from strategy.guerreiro import Guerreiro
from strategy.skills.luta_arco import UsoArco
from strategy.skills.luta_espada import LutaEspada
from strategy.skills.curar import Curar

cavaleiro = Guerreiro(LutaEspada(6))
arqueiro = Guerreiro(UsoArco(10))

cavaleiro.acao()
arqueiro.acao()
arqueiro.atributos()