class Partida():
    def __init__(self, jogador1, jogador2):
        self.__jogador1 = jogador1
        self.__jogador2 = jogador2
        self.__rodada = 0
        self.__vencedor = None

    def terminar_rodada(self):
        self.__rodada += 1


    def jogador_rodada(self):
        if self.__rodada % 2 != 0:
            return self.__jogador1
        else:
            return self.__jogador2


    def compra(self):
        if self.__rodada == 0:
            pass
        else:
            jogador = self.jogador_rodada()
            jogador.comprar_carta()


    def combate(self, carta, carta_inimiga, adversario):
        pass


    def condicao_vitoria(self):
        if (self.__jogador1.vida or self.__jogador2) == 0:
            return f"Jogador {self.__vencedor} venceu!"
