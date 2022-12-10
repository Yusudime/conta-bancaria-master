


class Conta:
    def __init__(self, numero:int, saldo:float):
        self.numero = numero
        self.saldo = saldo
        self.limite = 100
        self.extrato =  []
        self.op = 0
        self.adição = 0
        self.subratação = 0

    def getNumero(self):
        self.numero
        return self.numero

    def getSaldo(self):
        self.saldo += self.limite


        return self.saldo

    def getLimite(self):
        self.extrato
        return self.extrato

    def sacar(self, valor: float):
        if valor > 0:
            if valor < self.saldo:
                self.saldo -= valor
                print(self.getSaldo())
                self.adição += 1
                return True
            else:
                self.adição += 1
                print("Saldo Insufuciente")

                return False
        self.adição += 1
        return False
    def depositar(self, valor: float):
        if valor > 0:
            self.saldo += valor
            print(self.getSaldo())
            self.adição += 1
            return True


        else:
            self.adição += 1
           return False
        self.adição += 1
        return False

    def transferir(self, destino, valor:float):
        if destino != self.numero:
            if valor > 0:
                self.sacar()
                self.depositar()
                return True

        return False

    @property
    def verExtrato(self):
        self.adição + self.subratação = op
        for self.op < 10:
            if self.depositar():
                self.extrato.append('+')
            elif self.sacar():
                self.extrato.append('-')
        print(self.extrato)
        return self.extrato