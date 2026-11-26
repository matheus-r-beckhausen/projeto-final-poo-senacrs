from projeto_final_poo_senacrs.cartas.monstros.zumbi import Zumbi
from projeto_final_poo_senacrs.cartas.monstros.demonio import Demonio
from projeto_final_poo_senacrs.cartas.monstros.fada import Fada
from projeto_final_poo_senacrs.cartas.magia import Magia
from projeto_final_poo_senacrs.cartas.armadilha import Armadilha
from projeto_final_poo_senacrs.jogador import Jogador
from projeto_final_poo_senacrs.deck import Deck







jogador1 = Jogador("Matheus")

jogador2 = Jogador("teste")



for i in range(5):
    jogador1.comprar_carta()

print(jogador1.cartas_mao)
print(jogador1.qt_cartas_deck())
print(jogador2.qt_cartas_deck())

print()
jogador2.comprar_carta()
jogador1.cartas_mao[0].receber_bonus(500)
print(jogador1.cartas_mao[0].descricao())
print(jogador2.cartas_mao[0].descricao())

print()
print(jogador1.campo.magias_armadilhas_no_campo)
print(jogador1.campo.monstros_no_campo)
jogador1.jogar_carta(jogador1.cartas_mao[0])
print(jogador1.campo.magias_armadilhas_no_campo)
print(jogador1.campo.monstros_no_campo)


print()
print(jogador1.vida)
jogador1.receber_dano(500)
print(jogador1.vida)
jogador1.curar(500)
print(jogador1.vida)
jogador1.curar(500)
print(jogador1.vida)
jogador1.receber_dano(5000)
print(jogador1.vida)



# jogador1.embaralhar_deck()

# jogador1.comprar_carta()
# jogador1.comprar_carta()

# cartas_na_mao = jogador1.cartas_mao

# for carta in cartas_na_mao:
#     print(carta.descricao())


# print(jogador1.qt_cartas_deck())



###############
#Testes Cartas#
###############




# print()
# print(carta1.descricao())
# print(carta2.descricao())
# print(carta3.descricao())
# print()

# print()
# carta1.jogar(jogador1)
# carta2.jogar(jogador1)
# carta3.jogar(jogador1)
# print(carta1.descricao())
# print(carta2.descricao())
# print(carta3.descricao())
# print()

# print()
# jogador1.mandar_para_cemiterio(carta1)
# print(carta1.descricao())
# print(carta2.descricao())
# print(carta3.descricao())
# print(jogador1.cemiterio)
# print()

# print()
# jogador1.mandar_para_cemiterio(carta2)
# print(carta1.descricao())
# print(carta2.descricao())
# print(carta3.descricao())
# print(jogador1.cemiterio)
# print()

# print("===================================")
# print("===================================")

# print()
# print(carta6.descricao())
# print(carta7.descricao())
# print(carta8.descricao())
# print()


# print()
# carta6.jogar(jogador1)
# carta7.jogar(jogador1)
# carta8.jogar(jogador1)
# print(carta6.descricao())
# print(carta7.descricao())
# print(carta8.descricao())
# print(jogador1.campo.magias_armadilhas_no_campo)
# print()

# print()
# jogador1.mandar_para_cemiterio(carta6)
# print(jogador1.cemiterio)
# print()


# print("===================================")
# print("===================================")


# print()
# print(carta5.descricao())
# print(carta9.descricao())
# print(carta10.descricao())
# print()

# print()
# carta5.jogar(jogador1)
# print(jogador1.cemiterio)
# print()








##################
#Primeiros Testes#
##################


# carta1 = Demonio("Vampiro", 500)
# carta2 = Demonio("Sucubus", 400)
# carta3 = Demonio("Múmia", 600)
# carta4 = Fada("Aqua", 500)
# carta5 = Magia("Vida", None)
# carta6 = Armadilha("Defesa Absoluta", None, None)
# carta7 = Armadilha("Contrataque", None, None)
# carta8 = Armadilha("Teste", None, None)
# carta9 = Magia("Dano", None)
# carta10 = Magia("Comprar Carta", None)

# print(carta1.descricao())

# carta1.receber_bonus(100)
# print()
# print(carta1.descricao())

# carta1.remover_bonus(100)
# print()
# print(carta1.descricao())

# carta1.remover_todo_bonus()
# print()
# print(carta1.descricao())


# print()
# print(carta2.descricao())


# print("===================================")
# print("===================================")

# # print()
# # print(carta1.descricao())
# # print(carta2.descricao())
# # print(carta4.descricao())

# # campo.ativar_bonus_tipo_monstro([carta1, carta2, carta4])
# # print()
# # print(carta1.descricao())
# # print(carta2.descricao())
# # print(carta4.descricao())

# # campo.ativar_bonus_tipo_monstro([carta1, carta2, carta4])
# # print()
# # print(carta1.descricao())
# # print(carta2.descricao())
# # print(carta4.descricao())

# # carta1.receber_bonus(300)
# # carta2.receber_bonus(300)
# # carta4.receber_bonus(300)
# # print()
# # print(carta1.descricao())
# # print(carta2.descricao())
# # print(carta4.descricao())


# # campo.mandar_para_cemiterio(carta2)
# # campo.ativar_bonus_tipo_monstro([carta1, carta4])
# # print()
# # print(carta1.descricao())
# # print(carta2.descricao())
# # print(carta4.descricao())


# print()
# print("===================================")
# print("===================================")


# print()
# print(carta4.descricao())

# carta4.receber_bonus(300)
# print()
# print(carta4.descricao())

# campo.mandar_para_cemiterio(carta4)
# print()
# print(carta4.descricao())


# print()
# print("===================================")
# print("===================================")
# print()



