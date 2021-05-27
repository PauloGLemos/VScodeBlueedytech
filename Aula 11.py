"""lista_Contatos=[("nome","123,-456"),("nome2","456-789"),("nome3","123,-456"),("nome4","123,-456"),("nome5","123,-456")]
print(lista_Contatos)

print(type(lista_Contatos))

lista =["nome","123,-456"]
tupla =("nome","123,-456")
print(lista)
print(tupla)
print(type(lista))
print(type(tupla))

lista[0] = "Elemento2"
print(lista)

#1 Desafio

Nota1= float(input("Digite a nota 1: " ))
Nota2= float(input("Digite a nota 2: " ))
Nota3= float(input("Digite a nota 3: " ))
Nota4= float(input("Digite a nota 4: " ))

soma = Nota1+Nota2+Nota3+Nota4/4
print("Sua nota sera: ",soma)

Nome= float(input("Digite o seu nome: " ))
Media= soma

lista_Contatos=[("nome","123,-456"),("nome2","456-789"),("nome3","123,-456"),("nome4","123,-456"),("nome5","123,-456")]
print(lista_Contatos)

def somar():
    num1 = 20
    num2 = 30
    soma = num1 + num2
    print(soma)
somar()"""

"""lista=[1,2,3,4,5,6,7,8,9]
soma=[i **2 for i in lista]
for x in lista:
    for y in soma:  
        teste=(f"{x}:{y}")
        print(teste)"""
   
"""for elemento2 in soma:"""
"""for elemento3 in soma:"""
"""print(f"{elemento2}:{elemento3}")

resultado={a:a**2 for a in range(1,10)}

print (resultado)"""

Marvel = {"Tony Stark":"Iron Man","Bruce Banner":"Hulk","Chris Hemsworth":"Thor","Chris Evans":"CaptainAmerica"}

DC = {"Bruce Wayne":"Batman","Clark kent":"Superman","Diana":"WonderWoman","Jason Momoa":"Aquaman"}

for heroes in DC:
    print(heroes)
    Marvel[heroes] = DC[heroes]

print(Marvel)
"""
numero = float(input("Digite um numero: "))

while numero >= 2:
    numero += 1
    print("A")
else:
    print("B")"""
        
