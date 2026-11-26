import pkgutil, importlib
from projeto_final_poo_senacrs.cartas.monstro import Monstro
import projeto_final_poo_senacrs.cartas.monstros

for info in pkgutil.iter_modules(projeto_final_poo_senacrs.cartas.monstros.__path__):
    importlib.import_module("cartas.monstros." + info.name)


def carregar_tipos_monstros():
    monstros = {}
    for monstro in Monstro.__subclasses__():
        monstros[monstro.__name__] = monstro
    return monstros

def listar_tipos(self):
    nomes = {}
    for tecnico, classe in self._tipos_veiculos.items():
        nomes[tecnico] = getattr(classe, "NOME", tecnico)
    return nomes