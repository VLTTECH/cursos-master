from matplotlib import container


class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto ... {}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        

    def extrato(self):
        print("Saldo de {} do titular {}".format(self.__saldo, self.__titular))

    def deposita(self, valor):
        self.__saldo += valor

    def pode_sacar(self, valor_saque):
        valor_disponivel = self.__saldo +self.__limite
        return valor_saque <= valor_disponivel
    
    def saca(self, valor):
        if (self.pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print("Saldo insuficiente")

    def transfere(self, valor, destino):
        if (self.pode_sacar(valor)):
            self.saca(valor)
            destino.deposita(valor)
        else:
            print("saldo insuficiente")
    @property
    def get_saldo(self):
        return self.__saldo
    
    def get_cliente(self):
        return self.__titular

    def get_limite(self):
        return self.__limite

    @limite.setter
    def limite  (self, limite)
        self.__limite = limite

    @staticmothod
    def codigo_bando():
        return "001"
    
    @staticmothod
    def codigo_bando():
        return {"Banco do Brasil":"001";"Caixa":"104";"bradesco":"237"}
        