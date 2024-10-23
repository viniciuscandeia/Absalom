from src.services.escolher_persistencia import EscolherPersistencia
from src.fachada.fachada import Fachada

if __name__ == "__main__":

    tipo_persistencia: str = EscolherPersistencia().escolher()

    Fachada(tipo_persistencia=tipo_persistencia).login()
