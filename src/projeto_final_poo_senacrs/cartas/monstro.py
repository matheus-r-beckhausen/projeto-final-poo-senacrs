from abc import abstractmethod
from projeto_final_poo_senacrs.carta import Carta



class Monstro(Carta):
    def __init__(self, nome, ataque):
        super().__init__(nome)
        self.__ataque = ataque
        self.__modificador_ataque = 0
        

    @property
    def ataque(self):
        return self.__ataque + self.__modificador_ataque

    @property
    def modificador_ataque(self):
        return self.__modificador_ataque


    def receber_bonus(self, valor):
        self.__modificador_ataque += valor


    def remover_bonus(self, valor):
        self.__modificador_ataque -= valor


    def remover_todo_bonus(self):
        self.__modificador_ataque = 0


    def descricao(self):
        return f"Carta Monstro de nome {self.nome} e tipo {self.tipo()} com {self.ataque} de ataque total"


    def atacar(self, carta_inimiga, adversario):
        pass

    @abstractmethod
    def tipo(self):
        pass

    def campo_mudou(self, cartas):
        pass

    def inicio_turno(self, jogador, cartas):
        pass

    def final_batalha(self, adversario, cartas):
        pass


    def jogar(self, jogador):
        return jogador.campo.colocar_carta_monstro(self)