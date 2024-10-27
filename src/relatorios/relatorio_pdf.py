from doctest import UnexpectedException

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

from src.execoes.RelatorioError import RelatorioError
from src.relatorios.relatorio import Relatorio
from src.repositorios.gerenciadores.gerenciador_usuarios import GerenciadorUsuarios


class RelatorioPDF(Relatorio):
    def __init__(self, gerenciador_usuarios: GerenciadorUsuarios):
        super().__init__(gerenciador_usuarios=gerenciador_usuarios)

    def formatar_relatorio(self, data: dict):
        try:
            nome_arquivo = self.gerar_nome_arquivo() + ".pdf"

            c = canvas.Canvas(nome_arquivo, pagesize=letter)
            c.setFont("Helvetica", 12)
            c.drawString(100, 750, "Relatório de Usuários")
            c.drawString(100, 730, f"Total: {data['total']}")
            c.drawString(100, 710, f"Vendedores: {data['quantidade_vendedor']}")
            c.drawString(100, 690, f"Administradores: {data['quantidade_adm']}")
            c.drawString(100, 670, f"Gerentes: {data['quantidade_gerente']}")
            c.drawString(
                100, 650, f"Porcentagem de Vendedores: {data['porcentagemVendedores']}%"
            )
            c.drawString(
                100, 630, f"Porcentagem de Administradores: {data['porcentagemAdm']}%"
            )
            c.drawString(
                100, 610, f"Porcentagem de Gerentes: {data['porcentagemGerente']}%"
            )
            c.save()
        except UnexpectedException as e:
            raise RelatorioError(e)
