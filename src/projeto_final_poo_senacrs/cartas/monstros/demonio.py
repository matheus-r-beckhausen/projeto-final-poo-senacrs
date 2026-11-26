from projeto_final_poo_senacrs.cartas.monstro import Monstro

class Demonio(Monstro):
    def __init__(self, nome, ataque):
        super().__init__(nome, ataque)
        self.__bonus_tipo_status = False

    
    @property
    def bonus_tipo_status(self):
        return self.__bonus_tipo_status

    def alterar_bonus_tipo_status(self):
        self.__bonus_tipo_status = False if self.__bonus_tipo_status else True


    def tipo(self):
        return "Demonônio"

    def remover_todo_bonus(self):
        super().remover_todo_bonus()
        self.__bonus_tipo_status = False

    def campo_mudou(self, cartas):
        if len(cartas) <= 1:
            for carta in cartas:
                if carta.bonus_tipo_status:
                    carta.remover_bonus(200)
                    carta.alterar_bonus_tipo_status()
        else:
            for carta in cartas:
                if not carta.bonus_tipo_status:
                    carta.receber_bonus(200)
                    carta.alterar_bonus_tipo_status()