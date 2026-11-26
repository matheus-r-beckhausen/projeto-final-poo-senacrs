from projeto_final_poo_senacrs.carta import Carta



class Armadilha(Carta):
    def __init__(self, nome, efeito, gatilho):
        super().__init__(nome)
        self.__efeito = efeito
        self.__gatilho = gatilho

    def descricao(self):
        return f"Carta Armadilha de nome {self.nome} com efeito ... e gatilho ..."

    def ativar(self):
        pass

    def jogar(self, jogador):
        return jogador.campo.colocar_carta_armadilha(self)