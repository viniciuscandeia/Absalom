from src.fabricas import FabricaGerenciadorUsuarios
from src.relatorios.relatorio import Relatorio
from src.relatorios.relatorio_html import RelatorioHtml
from src.relatorios.relatorio_pdf import RelatorioPdf

if __name__ == '__main__':
    gerenciador_usuarios = FabricaGerenciadorUsuarios.criar_gerenciador(
        "db"
    )
    # relatorio = RelatorioHtml(gerenciador_usuarios)
    relatorio = RelatorioPdf(gerenciador_usuarios)
    relatorio.gerar_relatorio()