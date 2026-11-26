


class Campo():
    def __init__(self):
        self.__campos_monstros = 3
        self.__campos_magias_armadilhas = 2
        self.__monstros_no_campo = []
        self.__magias_armadilhas_no_campo = []


    @property
    def magias_armadilhas_no_campo(self):
         return self.__magias_armadilhas_no_campo[:]
    
    @property
    def monstros_no_campo(self):
        return self.__monstros_no_campo[:]
    
    def grupos_mosntros_por_tipo(self):
        grupos = {}

        for card in self.__monstros_no_campo:
            tipo = card.tipo()
            if tipo not in grupos:
                grupos[tipo] = []
            grupos[tipo].append(card)

        return grupos


    def atualizar_campo(self):
        grupos = self.grupos_mosntros_por_tipo()
        for tipo, lista in grupos.items():
                    lista[0].campo_mudou(lista)

    def colocar_carta_monstro(self, card):
        if len(self.__monstros_no_campo) < 3:
            if card not in self.__monstros_no_campo:
                self.__monstros_no_campo.append(card)
                self.atualizar_campo()
                return True
        return False
             
    def colocar_carta_armadilha(self, card):
        if len(self.__magias_armadilhas_no_campo) < 2:
            if card not in self.__magias_armadilhas_no_campo:
                self.__magias_armadilhas_no_campo.append(card)
                return True
        return False


    def remover_carta(self, card):
        if card in self.__monstros_no_campo:
            self.__monstros_no_campo.remove(card)
            card.remover_todo_bonus()
            self.atualizar_campo()
        elif card in self.__magias_armadilhas_no_campo:
            self.__magias_armadilhas_no_campo.remove(card)
            # self.atualizar_campo()
