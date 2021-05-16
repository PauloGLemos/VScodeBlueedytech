'''def imprime_oi():
    print("Oi")

imprime_oi()

global a
a = 10
print(a)

def soma(x, y):
    a = 20
    return x + y + a

x = soma(10,5)
#b = soma(a,5)
print(x)

def soma(x, y):
    global total
    total = x + y

    total = 10

    soma(3,5)
    total = 10
    print("Valor", total)

def aumento_salarial(salario, percentual):
        novo_salario = salario*percentual/100 + salario
        return

salario_fulano = aumento_salarial(5000,1)
print(salario_fulano)

import math

a = math.pi
print(a)'''




