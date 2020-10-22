from src.calculadora.models import Calculadora

calculadora = Calculadora(10)
calculadora.somar(20)

print(f'Valor após cálculo de soma: {calculadora.valor}')