from abc import ABC, abstractmethod



class Carta(ABC):
    def __init__(self, nome):
        self._nome = nome

    @abstractmethod
    def descricao(self):
        pass

    @property
    def nome(self):
        return self._nome

    @abstractmethod
    def jogar(self, jogador):
            pass
