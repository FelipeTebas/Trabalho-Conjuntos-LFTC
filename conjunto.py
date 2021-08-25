class Conjunto:
    def __init__(self, conjunto = []):
        self.conjunto = conjunto
        if self.validarConjunto() is False:
            raise

    def validarConjunto(self):
        for n in range(1,len(self.conjunto)):
            print(n)
            if self.conjunto[n-1] == self.conjunto[n]:
                return False
        return True

    def tamanho(self):
        return len(self.conjunto)

    def possui(self, numero):
        if numero in self.conjunto:
            return True
        return False

    def contem(self, conjuntoB):
        for i in conjuntoB.conjunto:
            if(i not in self.conjunto):
                return False
        return True

    def contem_propriamente(self, conjuntoB):
        if len(self.conjunto) != len(conjuntoB.conjunto):
            return self.contem(conjuntoB)
        return False

    def eh_igual(self, conjuntoB):
        if len(self.conjunto) == len(conjuntoB.conjunto):
            return self.contem(conjuntoB)
        return False

    def eh_vazio(conjuntoB):
        if len(conjuntoB.conjunto) == 0:
            return True
        return False

    def uniao(self, conjuntoB):
        novo = self.conjunto
        for i in conjuntoB.conjunto:
            if i not in self.conjunto:
                novo.append(i)
        return novo

    def intersecao(self, conjuntoB):
        novo = []
        for i in conjuntoB.conjunto:
            if i in self.conjunto:
                novo.append(i)
        return novo 

    def diferenca(self, conjuntoB):
        novo = []
        for i in self.conjunto:
            if i not in conjuntoB.conjunto:
                novo.append(i)
        return novo

    def complemento(self, conjuntoB):
        novo = []
        for i in conjuntoB.conjunto:
            if i not in self.conjunto:
                novo.append(i)
        return novo