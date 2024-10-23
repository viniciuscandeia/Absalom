import unittest
from src.entidades.entidades_usuarios import Usuario
from src.fabricas.fabrica_entidades_usuarios import FabricaEntidadesUsuarios
from src.fabricas.fabrica_gerenciadores_usuarios import FabricaGerenciadorUsuarios

class TestGerenciadorUsuarios(unittest.TestCase):

    def setUp(self):
        # Criar o gerenciador com estratégia RAM para os testes
        self.gerenciador = FabricaGerenciadorUsuarios.criar_gerenciador('ram')

        # Definir dados do usuário para testes
        self.dados_usuario = {
            'id': self.gerenciador.gerar_novo_id(),
            'nome': 'Vinicius',
            'username': 'viniciuscandeia12',
            'email': 'viniciuscandeia12@gmail.com',
            'senha': '0000',
            'id_loja': 1
        }
        # Criar instância de usuário
        self.usuario = FabricaEntidadesUsuarios().criar_entidade(
            tipo="administrador", dados=self.dados_usuario
        )

    # Teste 1: Adicionar um usuário
    def test_adicionar_usuario(self):
        self.gerenciador.adicionar(self.usuario)
        usuario_buscado = self.gerenciador.buscar(self.usuario.id_)
        self.assertEqual(usuario_buscado.username, 'viniciuscandeia12')

    # Teste 2: Adicionar e remover o mesmo usuário
    def test_adicionar_remover_usuario(self):
        self.gerenciador.adicionar(self.usuario)
        self.gerenciador.remover(self.usuario.id_)
        usuario_buscado = self.gerenciador.buscar(self.usuario.id_)
        self.assertIsNone(usuario_buscado)

    # Teste 3: Adicionar, editar e remover
    def test_adicionar_editar_remover_usuario(self):
        self.gerenciador.adicionar(self.usuario)
        novo_dados = self.dados_usuario.copy()
        novo_dados['nome'] = 'Vinicius Candeia Editado'
        usuario_editado = FabricaEntidadesUsuarios().criar_entidade(
            tipo="administrador", dados=novo_dados
        )
        self.gerenciador.editar(self.usuario.id_, usuario_editado)

        usuario_buscado = self.gerenciador.buscar(self.usuario.id_)
        self.assertEqual(usuario_buscado.nome, 'Vinicius Candeia Editado')

        self.gerenciador.remover(self.usuario.id_)
        usuario_buscado = self.gerenciador.buscar(self.usuario.id_)
        self.assertIsNone(usuario_buscado)

    # Teste 4: Verificar se existe
    def test_verificar_existencia_usuario(self):
        self.gerenciador.adicionar(self.usuario)
        self.assertTrue(
            self.gerenciador.verificar_existencia(self.usuario.id_))
        self.gerenciador.remover(self.usuario.id_)
        self.assertFalse(
            self.gerenciador.verificar_existencia(self.usuario.id_))

    # Teste 5: Validar o usuário
    def test_validar_usuario(self):
        self.gerenciador.adicionar(self.usuario)
        usuario_validado = self.gerenciador.validar(
            'viniciuscandeia12', '0000')
        self.assertIsNotNone(usuario_validado)
        self.assertEqual(usuario_validado.username, 'viniciuscandeia12')

if __name__ == '__main__':
    unittest.main()
