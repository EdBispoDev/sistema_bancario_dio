from conta import Conta

class Banco:
    def __init__(self, nome):
        self.nome = nome
        self.contas = {}

    def criar_conta(self, numero, titular):
        if numero not in self.contas:
            self.contas[numero] = Conta(numero, titular)
            print(f"Conta {numero} criada para {titular}.")
        else:
            print("Número de conta já existe.")

    def get_conta(self, numero):
        return self.contas.get(numero)

    def listar_contas(self):
        print(f"\n--- Contas no Banco {self.nome} ---")
        for numero, conta in self.contas.items():
            print(f"Conta {numero} - Titular: {conta.titular} - Saldo: R${conta.saldo}")