from src.fabricas import FabricaGerenciadorUsuarios
from src.relatorios.relatorio import Relatorio
from src.relatorios.relatorio_html import RelatorioHTML
from src.relatorios.relatorio_pdf import RelatorioPDF

if __name__ == '__main__':
    gerenciador_usuarios = FabricaGerenciadorUsuarios.criar_gerenciador(
        "db"
    )
    # relatorio = RelatorioHTML(gerenciador_usuarios)
    relatorio = RelatorioPDF(gerenciador_usuarios)
    relatorio.gerar_relatorio()