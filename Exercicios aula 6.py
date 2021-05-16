#1. Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.

"""def soma():
        var1 = int(input("Digite num1:" ))
        var2 = int(input("Digite num2:" ))
        var3 = int(input("Digite num3:" ))

        somas = (var1 + var2 + var3)   
        print(f"A soma dos valores é:", {somas})
soma()

#4. Faça um programa que calcule o salário de um colaborador na empresa XYZ. O 
#4. salário é pago conforme a quantidade de horas trabalhadas. 
#4. Quando um funcionário trabalha mais de 40 horas ele recebe um adicional de 1.5 nas horas extras trabalhadas.

def empresaXYZ():
    horas = int(input("Digite horas trabalhadas: "))

    if horas >= 40:
        print("voce recebera um extra de 1.5 por horas trabalhadas",  (horas * 1.5) * 100)
    else:
        print("seu salario e igual a", horas * 100)

empresaXYZ()"""

#5.	Faça um programa que calcule através de uma função o IMC de uma pessoa que tenha 1,68 e pese 75kg.
def IMC():
    peso = float(input("Digite seu peso" ))
    altura = float(input("Digite sua altura:" ))

    somas = (peso/(altura*altura))  
    print(round("seu IMC e:", somas),3)
IMC()
