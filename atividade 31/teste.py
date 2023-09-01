  #contador de lucro
vendas = []
# Função para mostrar o menu
def mostrar_menu():

    print("\n===== Bem Vindo ao sistema Amaurilton =====")
    print("\n===== Lista de Vendas =====")
    print("1. Realizar nova Venda")
    print("2. Listar Vendas")
    print("3. calcular porcentagem de lucro")
    print("4. Remover Venda do Sistema")
    print("5. Sair do Sistema")
    print("============================")

while True:
        mostrar_menu()
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            venda = (input("Digite a venda que deseja adicionar: "))
            vendas.append(venda)
            print(f"Venda '{venda}' adicionada com sucesso!")

        elif escolha == '2':
            print("\n===== Lista de Vendas =====")
            for index, venda in enumerate(vendas, start=1):
                print(f"{index} R$:{venda}")
            print("============================")


        elif escolha == '3':
             venda = float(input("digite o valor da venda: "))
             lucro = float(30)
             print(lucro*venda/100)


        elif escolha == '4':
            if len(vendas) == 0:
                print("Não há Vendas para remover.")
            else:
                index = int(input("Digite o número da Venda que deseja remover: "))
                if 1 <= index <= len(vendas):
                    venda_removida = vendas.pop(index - 1)
                    print(f"Venda '{venda_removida}' marcada como concluída!")
                else:
                    print("Número de venda inválido!")

        elif escolha == '5':
            print("Saindo do Sistema. Obrigado!")
            break

        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")






