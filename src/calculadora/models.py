class Calculadora:
    def __init__(self, valor: 'Valor inicial para cálculo'):
        self._valor = valor
    def somar(self, valor):
        self._valor += valor
    def limpar(self):
        self._valor = 0
    def dividir(self,valor):
        self._valor /= valor
    @property
    def valor(self):
        return self._valor