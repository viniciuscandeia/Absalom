from src.telas.telas_listar_usuarios import TelaListarAdministradores
from src.fabricas.fabrica_gerenciadores_usuarios import FabricaGerenciadorUsuarios

gerenciador = FabricaGerenciadorUsuarios.criar_gerenciador('db')
lista = gerenciador.listar('administrador')

TelaListarAdministradores.tela(lista)
