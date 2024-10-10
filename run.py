from src.fachada.fachada import Fachada
from src.views.view_escolha_persistencia import TelaEscolhaPersistencia

if __name__ == "__main__":
    retorno = TelaEscolhaPersistencia.pegar_persistencia()

    fachada = Fachada(retorno)
    fachada.login()
