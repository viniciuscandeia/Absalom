from src.telas.gerenciador_telas import GerenciadorTelas


class EscolherPersistencia:

    @classmethod
    def escolher(cls) -> str:
        retorno: dict = {}
        while True:
            retorno: dict = GerenciadorTelas.escolher_persistencia()
            if retorno["opcao"] in ["1", "2"]:
                break

        match retorno["opcao"]:
            case "1":  # RAM
                return "ram"
            case "2":  # DB
                return "db"
