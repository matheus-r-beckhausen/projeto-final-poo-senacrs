from projeto_final_poo_senacrs.cartas.monstro import Monstro

class Humano(Monstro):
    def tipo(self):
        return "Humano"

    def inicio_turno(self, jogador, cartas):
        pass