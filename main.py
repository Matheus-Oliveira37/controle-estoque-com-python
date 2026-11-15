from produtos import *
from time import sleep
from rich import print
from rich.panel import Panel
from rich.table import Table
from rich.console import Console


atraso = sleep(0.2)

while True:

    painel = Panel(f"""
    [dark_sea_green2]1[/] - [italic]Cadastrar Produto
    [dark_sea_green2]2[/] - Listar Produtos
    [dark_sea_green2]3[/] - Buscar Produto
    [dark_sea_green2]4[/] - Atualizar Estoque
    [dark_sea_green2]5[/] - Excluir Produto
    [dark_sea_green2]6[/] - Produto com Estoque Baixo
    [dark_sea_green2]7[/] - Ordenar por Preço
    [dark_sea_green2]8[/] - Valor Total dos Produtos
    [dark_sea_green2]9[/] - Exportar Produtos para CSV
    [bold red3]10[/] - Sair""",
                   title="CONTROLE DE ESTOQUE",
                   border_style="bold green",
                   width=40,
                   height=14

                   )
    
    print(painel)
    
    

    opcao = input("\nEscolha uma opção: ")

    if opcao == "1":

        nome = input("Nome: ")
        preco = float(input("Preço: "))
        quantidade = int(input("Quantidade: "))

        cadastrar_produtos(nome, preco, quantidade)
        
        sleep(2)
        print("\n")


    elif opcao == "2":

        produtos = listar_produtos()

        tabela = Table(
            title="ESTOQUE",
            show_header=True,
            header_style="bold cyan",
            border_style="bold green"
        )

        tabela.add_column("ID")
        tabela.add_column("Nome")
        tabela.add_column("Preço")
        tabela.add_column("Quantidade", justify="center")
        tabela.add_column("Data")

        for produto in produtos:
            
            qtd = produto[3]
            
            if qtd < 10:
                qtd = f"[bold red]{qtd}[/]"
                
            else:
                qtd = f"[green]{qtd}[/]"

            tabela.add_row(
                str(produto[0]),  # id
                produto[1],       # nome
                f"R$ {produto[2]:.2f}",
                str(qtd),  # quantidade
                str(produto[4])   # data
            )

        print(tabela)
        
        sleep(2)
        print("\n")

    elif opcao == "3":

        nome = input("Produto: ")
        produtos = buscar_produto(nome)
        
        if not produtos:
            print("[bold red italic]Nenhum produto encontrado.")
            sleep(2)
            continue
        
        
        tabela = Table(
            title=f"{nome}",
            show_header=True,
            header_style="Bold cyan"
        )
                
        
        tabela.add_column("ID")
        tabela.add_column("Nome")
        tabela.add_column("Preço")
        tabela.add_column("Quantidade", justify="center")
        tabela.add_column("Data")
        
        for produto in produtos:
            
            qtd = produto[3]
                            
            if qtd < 10:
                qtd = f"[bold red]{qtd}[/]"
            else:
                qtd = f"[green]{qtd}[/]"
            
            tabela.add_row(
                str(produto[0]),
                str(produto[1]),
                f"R$ {produto[2]:.2f}",
                str(f"{qtd}"),
                str(produto[4])
            )
            
        print(tabela)
        
        sleep(2)
        print("\n")

    elif opcao == "4":
        id_produto = int(input("ID: "))
        nova_qtd = int(input("Nova quantidade: "))

        atualizar_estoque(id_produto, nova_qtd)
        
        sleep(2)
        print("\n")

    elif opcao == "5":
        id_produto = int(input("ID: "))
        excluir_produto(id_produto)
        
        sleep(2)
        print("\n")

    elif opcao == "6":

        produtos = estoque_baixo()

        tabela = Table(
            title="ESTOQUE BAIXO",
            show_header=True,
            header_style="bold cyan",
            border_style="bold green"
        )

        tabela.add_column("ID")
        tabela.add_column("Nome")
        tabela.add_column("Preço")
        tabela.add_column("Quantidade", justify="center", style="bold red")
        tabela.add_column("Data")

        for produto in produtos:

            tabela.add_row(
                str(produto[0]),  # id
                produto[1],       # nome
                f"R$ {produto[2]:.2f}",
                str(produto[3]),  # quantidade
                str(produto[4])   # data
            )

        print(tabela)
        
        sleep(2)
        print("\n")

    elif opcao == "7":
        
        produtos = order_preco()
        
        tabela = Table(
            title="ORDENADO POR PREÇO",
            show_header=True,
            header_style="Bold cyan"
        )
                        
                
        tabela.add_column("ID")
        tabela.add_column("Nome")
        tabela.add_column("Preço")
        tabela.add_column("Quantidade", justify="center")
        tabela.add_column("Data")
                
        for produto in produtos:
                    
            qtd = produto[3]
                                    
            if qtd < 10:
                qtd = f"[bold red]{qtd}[/]"
            else:
                qtd = f"[green]{qtd}[/]"
                    
            tabela.add_row(
                str(produto[0]),
                str(produto[1]),
                f"R$ {produto[2]:.2f}",
                str(f"{qtd}"),
                str(produto[4])
            )
                    
        print(tabela)
        
        sleep(2)
        print("\n")

    elif opcao == "8":

        console = Console()

        total = valor_total()

        console.print(
            Panel(
                f"[green]R${total:.2f}[/]",
                title="VALOR TOTAL EM ESTOQUE",
                width=40,
                border_style="bold green"
            )
        )
        
        sleep(2)
        print("\n")
        
    elif opcao == "9":
        
        exportar_csv()
        
        painel = Panel(
            "Arquivo salvo como [italic]produtos.csv[/]",
            title="EXPORTAÇÃO CONCLUÍDA",
            border_style="green",
            width=40
            )
        
        print(painel)
        sleep(2)

    elif opcao == "10":
        print(f"[italic ]Encerrando")
        sleep(1)
        print(f"[yellow].[/]")
        sleep(1)
        print(f"[bold color(208)].[/]")
        sleep(1)
        print(f"[bold red].[/]")
        sleep(1)
        break

    else:
        print("[bold red italic]Opção inválida.[/]")
        sleep(1)
