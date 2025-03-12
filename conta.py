class Conta:
    def __init__(self, numero, titular, saldo=0):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.transacoes = []

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.transacoes.append(f"Depósito: +{valor}")
            print(f"Depósito de R${valor} realizado com sucesso.")
        else:
            print("Valor de depósito inválido.")

    def sacar(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            self.transacoes.append(f"Saque: -{valor}")
            print(f"Saque de R${valor} realizado com sucesso.")
        else:
            print("Saldo insuficiente ou valor de saque inválido.")

    def extrato(self):
        print(f"\n--- Extrato da Conta {self.numero} ---")
        print(f"Titular: {self.titular}")
        print("Transações:")
        for transacao in self.transacoes:
            print(transacao)
        print(f"Saldo atual: R${self.saldo}\n")