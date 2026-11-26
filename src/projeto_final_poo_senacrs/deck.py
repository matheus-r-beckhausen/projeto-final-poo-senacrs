import random



class Deck():
    def __init__(self, cartas):
        self.__cartas = cartas[:]

    
    def embaralhar(self):
        random.shuffle(self.__cartas)


    def comprar_carta(self):
        if len(self.__cartas) >= 1:
            carta_removida = self.__cartas.pop(0)
            return carta_removida
        else:
            return False

    def cartas_no_deck(self):
        return len(self.__cartas)