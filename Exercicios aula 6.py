#1. Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.
#teste

def soma():
        var1 = int(input("Digite num1:" ))
        var2 = int(input("Digite num2:" ))
        var3 = int(input("Digite num3:" ))

        somas = (var1 + var2 + var3)   
        print(f"A soma dos valores é:", {somas})
soma()

def empresaXYZ():
    horas = int(input("Digite horas trabalhadas: "))

    if horas >= 40:
        print("voce recebera um extra de 1.5 por horas trabalhadas",  (horas * 1.5) * 100)
    else:
        print("seu salario e igual a", horas * 100)

empresaXYZ()
