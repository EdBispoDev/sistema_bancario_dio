from banco import Banco

def menu():
    print("\n--- Banco DIO ---")
    print("1. Criar Conta")
    print("2. Depositar")
    print("3. Sacar")
    print("4. Ver Extrato")
    print("5. Listar Contas")
    print("6. Sair")
    return input("Escolha uma opção: ")

def main():
    banco = Banco("Banco DIO")

    while True:
        opcao = menu()

        if opcao == "1":
            numero = int(input("Número da conta: "))
            titular = input("Nome do titular: ")
            banco.criar_conta(numero, titular)

        elif opcao == "2":
            numero = int(input("Número da conta: "))
            valor = float(input("Valor do depósito: "))
            conta = banco.get_conta(numero)
            if conta:
                conta.depositar(valor)
            else:
                print("Conta não encontrada.")

        elif opcao == "3":
            numero = int(input("Número da conta: "))
            valor = float(input("Valor do saque: "))
            conta = banco.get_conta(numero)
            if conta:
                conta.sacar(valor)
            else:
                print("Conta não encontrada.")

        elif opcao == "4":
            numero = int(input("Número da conta: "))
            conta = banco.get_conta(numero)
            if conta:
                conta.extrato()
            else:
                print("Conta não encontrada.")

        elif opcao == "5":
            banco.listar_contas()

        elif opcao == "6":
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()