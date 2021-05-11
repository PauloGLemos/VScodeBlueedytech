def soma():
    var1 = int(input("Digite num1:" ))
    var2 = int(input("Digite num2:" ))
    var3 = var1 + var2
    print (var3)

def tomar_banho():
    print("Tirar a roupa")
    print("Abrir o chuveiro")
    print("Se lavar")
    print("Fechar o chuveiro")
    print("Se secar")
    print("colocar uma roupa limpa")

    var1 = int(input("Digite num1:" ))
    var2 = int(input("Digite num2:" ))
    var3 = var1 + var2
    if var3 >= 10:
            print("É maior ou igual a 10")
    else:
            print("É menor que 10")

tomar_banho()
print("\nAgora bou fazer de novo\n")

Nome = input("Qual seu nome: ".capitalize)
print("Seu nome e", Nome)

'''sujo = input("Voce esta sujo? S/N")
if sujo == " 1S":
    tomar_banho()
else:
    print("voce esta cheroso")'''

soma()