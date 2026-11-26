from projeto_final_poo_senacrs.deck import Deck
from projeto_final_poo_senacrs.cartas.magia import Magia
from projeto_final_poo_senacrs.cartas.armadilha import Armadilha
from projeto_final_poo_senacrs.cartas.tipos_monstros import carregar_tipos_monstros

MONSTROS = [
    ("Demonio", "Vampiro", 400),
    ("Demonio", "Cavaleiro Negro", 500),
    ("Demonio", "Sucubus", 400),
    ("Demonio", "Múmia", 400),
    ("Demonio", "Vampiro", 400),
    ("Demonio", "Cavaleiro Negro", 500),
    ("Fada", "Aqua", 400),
    ("Fada", "Aqua", 400),
    ("Fada", "", 400),
    ("Fada", "", 400),
    ("Humano", "Cavaleiro", 500),
    ("Zumbi", "Lich", 600),
    ("Zumbi", "Horda Zumbi", 500),
    ("Humano", "Cavaleiro", 500),
    ("Humano", "Rei", 700),
    ("Humano", "Estrategista", 600),
    ("Humano", "Mago", 600),
    ("Zumbi", "Lich", 600),
    ("Zumbi", "Horda Zumbi", 500),
    ("Zumbi", "Cavalo Zumbi", 400),
    ("Zumbi", "Zumbi", 400)
]


MAGIAS = ["Poção de Cura", "Poção de Cura", "Lâmina Flamejante", "Lâmina Flamejante", "Pote da ganância"]

ARMADILHAS = ["Escudo Refletor", "Contra Ataque", "Escudo Refletor", "Contra Ataque"]



def montar_deck():
    tipos = carregar_tipos_monstros()
    cartas = []
    for tipo, nome, atk in MONSTROS:
        classe = tipos[tipo]
        monstro = classe(nome, atk)
        cartas.append(monstro)

    for nome in MAGIAS:
        magia = Magia(nome, None)
        cartas.append(magia)

    for nome in ARMADILHAS:
        armadilha = Armadilha(nome, None, None)
        cartas.append(armadilha)
    
    return Deck(cartas)