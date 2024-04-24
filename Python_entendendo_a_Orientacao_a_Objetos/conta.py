class Conta():


    @staticmethod
    def codigo_banco():
        return "104"
   
    def __init__(self, conta, titular, saldo, limite):
        self.__conta = conta
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite


    def extrato (self):
        return self.__saldo
    
    def deposito (self, valor):
        self.__saldo += valor
    
    def saque (self, valor_a_sacar):
        if(self.__pode_sacar(valor_a_sacar)):
            self.__saldo -= valor_a_sacar
        else:
            print("Valor de saque superior ao valor do saldo da conta!")

    def tranfere (self, valor, conta_destino):
        self.saque(valor)
        conta_destino.deposito(valor)

    @property
    def saldo(self):
        return self.__saldo
    
    @property
    def limite(self):
        return self.__limite
    @property
    def titular(self):
        return self.__titular

    @limite.setter
    def limite(self, novo_limite):
        self.__limite = novo_limite
        
    def __pode_sacar (self, valor_a_sacar):
        return valor_a_sacar <= self.__saldo
        
conta4 = Conta(3728, "Elizabeth", 25000.0, 50000.0)
conta5 = Conta(3792, "Victor", 17000.0, 34000.0)