#06 - Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:

   # "Telefonou para a vítima?"

   # "Esteve no local do crime?"

   # "Mora perto da vítima?"

   # "Devia para a vítima?"

   # "Já trabalhou com a vítima?" 

# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 

   # Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita",

   # Entre 3 e 4 como "Cúmplice" e 5 como "Assassino". 

   # Caso contrário, ele será classificado como "Inocente".

lista1 =  ["Telefonou para a vítima ? ","DEsteve no local do crime ? ","Mora perto da vítima ? ","Devia para a vítima ? ","Já trabalhou com a vítima ? "]

B = 0
for C in lista1:
    A = input(C).lower()
    if A == "sim":
        B += 1

    if B < 2:
        print("Inocente")
    elif B == 2:
        print("Suspeita")
    elif B <= 4:
        print("Cúmplice")
    else:
        print("Assassino")



