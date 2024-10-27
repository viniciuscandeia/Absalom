from src.fabricas.fabrica_entidades import FabricaEntidades
from src.fabricas.fabrica_repositorio_loja import FabricaGerenciadorLojas
from src.memento.loja.caretaker_loja import CaretakerLoja
from src.memento.loja.originator_loja import OriginatorLoja
from src.entidades.entidade_loja import Loja
from src.memento.memento import Memento

if __name__ == "__main__":
    informacoes: dict = {}
    informacoes["id"] = 2
    informacoes["nome"] = "nome"
    informacoes["endereco"] = "nome"

    informacoes2: dict = {}
    informacoes2["id"] = 2
    informacoes2["nome"] = "nome 2"
    informacoes2["endereco"] = "nome 2"

    informacoes3: dict = {}
    informacoes3["id"] = 3
    informacoes3["nome"] = "nome 3"
    informacoes3["endereco"] = "nome 3"

    loja:Loja = FabricaEntidades.criar_entidade('loja', informacoes)
    loja2 =  FabricaEntidades.criar_entidade('loja', informacoes2)
    loja3 =  FabricaEntidades.criar_entidade('loja', informacoes3)

    originator = OriginatorLoja(loja)
    caretaker = CaretakerLoja()
    caretaker.add_memento(originator.create_memento())
    print('estado inicializado')
    print(originator.get_state())
    print('estado inicializado')
    originator.set_state(loja2)
    loja.setNome('2312323')
    originator.set_state(loja2)
    print(originator.get_state())
    originator.set_state(loja3)
    print(originator.get_state())

    originator.restore(caretaker.get_memento(0))
    print('estado restaurado')
    print(originator.get_state())
    print('mementos')
    print(caretaker.get_mementos())

