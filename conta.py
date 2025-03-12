class Conta():
    def __init__(self, numero, titular, saldo):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.transacoes = []
        
    def depositar(self, valor):
        
        if valor > 0:
            self.saldo += 0
            self.transacoes.append(f'Depósito: +{valor}')
            print(f'Depósito de R${valor} realizado com sucesso.')
        else:
            print('Valor do depósito inválido')
        
    def sacar(self, valor):
        if = < valor <= self.saldo:
            self.saldo -= valor
            self.transacoes.append(f'Saque: -{valor}')
            print(f'Saque de R${valor} realizado com sucesso.')
            else:
            print('Saldo insuficiente ou Valor de saque inválido.')
            
    def extrato(self):
        print(f'Extrato da conta {self.numero} - Titular: {self.titular}')
        for transacao in self.transacoes:
            print(transacao)
        print(f'Saldo atual: R${self.saldo}\n')           
        