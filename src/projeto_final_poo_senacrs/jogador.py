from projeto_final_poo_senacrs.campo import Campo
from projeto_final_poo_senacrs.catalogo import montar_deck




class Jogador():
    def __init__(self, nome, vida=4000):
        self.__nome = nome
        self.__vida_maxima = vida
        self.__vida = vida
        self.__deck = montar_deck()
        self.__cemiterio = []
        self.__campo = Campo()
        self.__cartas_mao = []


    @property
    def vida(self):
        return self.__vida

    @property
    def nome(self):
        return self.__nome

    @property
    def cartas_mao(self):
        return self.__cartas_mao[:]

    @property
    def cemiterio(self):
        return self.__cemiterio[:]

    @property
    def campo(self):
        return self.__campo


    def embaralhar_deck(self):
        self.__deck.embaralhar()

    def qt_cartas_deck(self):
        qt= self.__deck.cartas_no_deck()
        return qt

    def receber_dano(self, valor):
        if valor > self.__vida:
            self.__vida = 0
        else:
            self.__vida -= valor


    def curar(self, valor):
        if (valor + self.__vida) > self.__vida_maxima:
            self.__vida = self.__vida_maxima
        else:
            self.__vida += valor


    def escolher_acao(self):
        pass


    def mandar_para_cemiterio(self, card):
        self.campo.remover_carta(card)
        if card not in self.__cemiterio:
            self.__cemiterio.append(card)


    def comprar_carta(self):
        carta = self.__deck.comprar_carta()
        if carta:
            self.__cartas_mao.append(carta)
            return True
        return False

    def jogar_carta(self, carta):
        if carta in self.__cartas_mao:
            resultado = carta.jogar(self)
            if resultado:
                self.__cartas_mao.remove(carta)
                return True
            return False
        return False
