from projeto_final_poo_senacrs.carta import Carta



class Magia(Carta):
    def __init__(self, nome, efeito):
        super().__init__(nome)
        self.__efeito = efeito

    def descricao(self):
        return f"Carta Magia de nome {self.nome} com efeito ..."

    def ativar(self, carta_alvo):
        pass

    def jogar(self, jogador):
        jogador.mandar_para_cemiterio(self)
        return True