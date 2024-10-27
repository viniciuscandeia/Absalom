from src.relatorios.relatorio import Relatorio
from src.repositorios.gerenciadores.gerenciador_usuarios import GerenciadorUsuarios


class RelatorioHtml(Relatorio):
    def __init__(self, gerenciador_usuarios: GerenciadorUsuarios):
        super().__init__(gerenciador_usuarios=gerenciador_usuarios)

    def formatar_relatorio(self, data: dict):
        nome_arquivo = f"relatorio_{self.gerar_nome_arquivo()}.html"

        html_content = f"""
        <!DOCTYPE html>
        <html lang="pt-br">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Relatório de Usuários</title>
            <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
            <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet">
            <style>
                body {{
                    background-color: #32435e;
                    font-family: 'Poppins', sans-serif;
                }}
                
                #relatorioChart {{
                    
                    height: 400px !important;
                    max-width: 100%;
                    max-height: 100%;
                }}
                 @media (min-width: 1024px) {{
                    #relatorioChart {{
                        height: 100% !important;
                    }}
                }}
            </style>
        </head>
        <body>
            <h1 style="color:white;">Relatório de Usuários</h1>
            <p style="color:white;">Total de Usuários: {data['total']}</p>
            <p style="color:white;">Total de Administradores: {data['quantidade_adm']} ({data['porcentagemAdm']:.2f}%)</p>
            <p style="color:white;">Total de Gerentes: {data['quantidade_gerente']} ({data['porcentagemGerente']:.2f}%)</p>
            <p style="color:white;">Total de Vendedores: {data['quantidade_vendedor']} ({data['porcentagemVendedores']:.2f}%)</p>
            <canvas id="relatorioChart"></canvas>
            <script>
              const data = {{
                    labels: ['Administradores', 'Gerentes', 'Vendedores'],
                    datasets: [{{
                        label: 'Distribuição de Usuários',
                        data: [{data['quantidade_adm']}, {data['quantidade_gerente']}, {data['quantidade_vendedor']}],
                        backgroundColor: [
                            'rgba(255, 99, 132)',  // Administradores
                            'rgba(54, 162, 235)',  // Gerentes
                            'rgba(75, 192, 192)'   // Vendedores
                        ],
                        borderColor: [
                            'rgba(255, 99, 132, 1)',  // Administradores
                            'rgba(54, 162, 235, 1)',  // Gerentes
                            'rgba(75, 192, 192, 1)'   // Vendedores
                        ],
                        borderWidth: 1
                    }}]
                }};

                // Configuração do gráfico
                const config = {{
                    type: 'bar',
                    data: data,
                    options: {{
                        responsive: true,
                        maintainAspectRatio: true,
                        plugins: {{
                            legend: {{
                                display: false
                            }},
                            title: {{
                                display: true,
                                text: 'Distribuição de Usuários',
                                color: '#FFF' 
                            }}
                        }},
                        scales: {{
                            x: {{  
                                ticks: {{
                                    color: '#FFF'  
                                }}
                            }},
                            y: {{  
                                ticks: {{
                                    color: '#FFF' 
                                }}
                            }}
                        }}
                    }}
                }};

                // Renderiza o gráfico
                const ctx = document.getElementById('relatorioChart').getContext('2d');
                new Chart(ctx, config);
            </script>
        </body>
        </html>
        """

        # Escreve o conteúdo HTML em um arquivo
        with open(nome_arquivo, "w", encoding="utf-8") as file:
            file.write(html_content)

        print(f"Relatório gerado: {nome_arquivo}")
