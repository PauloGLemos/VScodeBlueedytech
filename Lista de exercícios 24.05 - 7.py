#07 - Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. 
# No final, mostre os valores pares e ímpares em ordem crescente.

Lista1 = ["  ","  ","  ","  ","  ","  ","  "]
Lista1.sort()

A = 0

while A < len(Lista1):
    Lista1[A] = int (input("Digite 7 numeros : "))
    A+=1
print(Lista1)

for A in Lista1(range(0,7)):
    if (A % 2) == 0:
        print(Lista1)
    else:
        print(Lista1)
  